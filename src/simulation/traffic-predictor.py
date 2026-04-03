"""Predictive Traffic Intelligence Engine.

Implements rolling Markov-based vehicle density forecasting, congestion
probability estimation five minutes ahead, and RSU sensor integration.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Deque, Dict, List, Sequence, Tuple


DENSITY_STATES: Tuple[str, str, str] = ("low", "medium", "high")


@dataclass(frozen=True)
class RSUSensorReading:
    """Single RSU node input at a point in time."""

    node_id: str
    vehicle_density: float
    arrival_rate: float
    timestamp: datetime


class PredictiveTrafficIntelligenceEngine:
    """Rolling Markov predictor for near-term congestion intelligence."""

    def __init__(self, window_size: int = 120) -> None:
        # ~5 minutes of samples when readings arrive every ~2.5 seconds.
        self.window_size = max(2, window_size)
        self._state_history: Deque[str] = deque(maxlen=self.window_size)
        self._readings_history: Deque[RSUSensorReading] = deque(maxlen=self.window_size)

        self._transition_counts: Dict[str, Dict[str, float]] = {
            state: {next_state: 1.0 for next_state in DENSITY_STATES}
            for state in DENSITY_STATES
        }

    @staticmethod
    def _state_from_density(vehicle_density: float) -> str:
        if vehicle_density < 0.33:
            return "low"
        if vehicle_density < 0.66:
            return "medium"
        return "high"

    def ingest_rsu_inputs(self, sensor_inputs: Sequence[RSUSensorReading]) -> None:
        """Integrate RSU node readings into the rolling model."""
        for reading in sensor_inputs:
            current_state = self._state_from_density(reading.vehicle_density)
            previous_state = self._state_history[-1] if self._state_history else None

            self._readings_history.append(reading)
            self._state_history.append(current_state)

            if previous_state is not None:
                self._transition_counts[previous_state][current_state] += 1.0

    def _transition_probabilities(self, state: str) -> Dict[str, float]:
        counts = self._transition_counts[state]
        total = sum(counts.values())
        return {next_state: count / total for next_state, count in counts.items()}

    def _step_state_distribution(self, state_distribution: Dict[str, float]) -> Dict[str, float]:
        next_distribution = {state: 0.0 for state in DENSITY_STATES}
        for state, weight in state_distribution.items():
            transitions = self._transition_probabilities(state)
            for next_state, transition_prob in transitions.items():
                next_distribution[next_state] += weight * transition_prob
        return next_distribution

    def _forecast_density_distribution(self, steps_ahead: int) -> Dict[str, float]:
        if not self._state_history:
            return {"low": 1 / 3, "medium": 1 / 3, "high": 1 / 3}

        distribution = {state: 0.0 for state in DENSITY_STATES}
        distribution[self._state_history[-1]] = 1.0

        for _ in range(max(1, steps_ahead)):
            distribution = self._step_state_distribution(distribution)

        return distribution

    def predict_congestion_probability_5min(self, sample_period_seconds: int = 5) -> float:
        """Predict congestion probability five minutes ahead.

        Congestion_prob = Σ(vehicle_density × arrival_rate)
        computed over RSU inputs and adjusted by Markov high-density likelihood.
        """
        if not self._readings_history:
            return 0.0

        steps_ahead = max(1, 300 // max(1, sample_period_seconds))
        future_distribution = self._forecast_density_distribution(steps_ahead=steps_ahead)

        # Formula requested in task:
        base_probability = sum(
            reading.vehicle_density * reading.arrival_rate
            for reading in self._readings_history
        )
        base_probability /= len(self._readings_history)

        # Markov signal scales probability by chance of high-density state.
        high_density_weight = future_distribution["high"]
        congestion_probability = min(1.0, max(0.0, base_probability * (1.0 + high_density_weight)))
        return congestion_probability

    def run_cycle(self, sensor_inputs: Sequence[RSUSensorReading]) -> Dict[str, float]:
        self.ingest_rsu_inputs(sensor_inputs)
        congestion_probability = self.predict_congestion_probability_5min()

        print("TRAFFIC_INTELLIGENCE: PREDICTIVE_MODEL_ACTIVE")

        return {
            "timestamp": datetime.now(timezone.utc).timestamp(),
            "congestion_probability_5min": congestion_probability,
        }


if __name__ == "__main__":
    engine = PredictiveTrafficIntelligenceEngine(window_size=120)
    now = datetime.now(timezone.utc)

    sample_inputs: List[RSUSensorReading] = [
        RSUSensorReading("rsu-1", vehicle_density=0.72, arrival_rate=0.89, timestamp=now),
        RSUSensorReading("rsu-2", vehicle_density=0.61, arrival_rate=0.74, timestamp=now),
        RSUSensorReading("rsu-3", vehicle_density=0.48, arrival_rate=0.67, timestamp=now),
    ]

    result = engine.run_cycle(sample_inputs)
    print(result)
