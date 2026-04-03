#include <array>
#include <atomic>
#include <cstddef>
#include <cstdint>
#include <iostream>

namespace infra {

struct TelemetryEvent {
  std::uint64_t id{0};
  std::int64_t timestamp_ms{0};
  std::array<char, 128> payload{};
};

class BurstTelemetryBuffer {
 public:
  static constexpr std::size_t kBurstRatePerSecond = 50000;
  static constexpr std::size_t kCapacity = kBurstRatePerSecond * 2;

  using OverflowHandler = void (*)(std::size_t queued, std::size_t capacity, void* context);

  BurstTelemetryBuffer() = default;

  void set_overflow_handler(OverflowHandler handler, void* context = nullptr) {
    overflow_handler_ = handler;
    overflow_context_ = context;
  }

  bool enqueue(const TelemetryEvent& event) {
    const std::size_t current_count = count_.load(std::memory_order_acquire);
    if (current_count >= kCapacity) {
      trigger_overflow(current_count);
      return false;
    }

    const std::size_t write_index = head_.fetch_add(1, std::memory_order_acq_rel) % kCapacity;
    ring_[write_index] = event;
    const std::size_t new_count = count_.fetch_add(1, std::memory_order_acq_rel) + 1;

    if (new_count >= overflow_threshold()) {
      trigger_overflow(new_count);
    }

    return true;
  }

  bool dequeue(TelemetryEvent& out) {
    const std::size_t current_count = count_.load(std::memory_order_acquire);
    if (current_count == 0) {
      return false;
    }

    const std::size_t read_index = tail_.fetch_add(1, std::memory_order_acq_rel) % kCapacity;
    out = ring_[read_index];
    count_.fetch_sub(1, std::memory_order_acq_rel);
    return true;
  }

  [[nodiscard]] std::size_t size() const {
    return count_.load(std::memory_order_acquire);
  }

  [[nodiscard]] constexpr std::size_t capacity() const {
    return kCapacity;
  }

 private:
  [[nodiscard]] static constexpr std::size_t overflow_threshold() {
    return static_cast<std::size_t>(static_cast<double>(kCapacity) * 0.95);
  }

  void trigger_overflow(std::size_t queued) {
    std::cerr << "BUFFER_STATE: BURST_CAPACITY_PROTECTED"
              << " queued=" << queued
              << " capacity=" << kCapacity
              << '\n';

    if (overflow_handler_) {
      overflow_handler_(queued, kCapacity, overflow_context_);
    }
  }

  std::array<TelemetryEvent, kCapacity> ring_{};
  std::atomic<std::size_t> head_{0};
  std::atomic<std::size_t> tail_{0};
  std::atomic<std::size_t> count_{0};
  OverflowHandler overflow_handler_{nullptr};
  void* overflow_context_{nullptr};
};

}  // namespace infra
