# KUP Claude Code Execution Prompts
## 6 Autonomous Execution Templates for KUP Repos

---

## PROMPT 1: kup-ai-systems-lab
### Executive Brief
Build KUP brand positioning docs, digital twin architecture specs, and stakeholder narratives. Output: 4 markdown documents ready for investor + NHAI + research institution consumption.

### Directory Structure (create if missing)
```
kup-ai-systems-lab/
├── README.md
├── BRAND_POSITIONING.md
├── DIGITAL_TWIN_ARCHITECTURE.md
├── WHY_KUTCH.md
├── STAKEHOLDER_NARRATIVES.md
├── logo.svg
├── brand-guidelines.md
└── pitch-deck-outline.txt
```

### Tasks (Sequential)

**Task 1.1: Brand Positioning Document**
- File: `BRAND_POSITIONING.md`
- Output: 1,200 words
- Structure:
  - Problem statement: "95% GenAI projects fail in extreme climate environments"
  - Solution: "KUP AI Systems Lab: Data-centric AI infrastructure for Kutch (20–48°C, 1M vehicle passages/hour)"
  - Positioning statement: "Building resilient AI for infrastructure in extreme environments"
  - Market opportunity: ₹100L Year 1, ₹1000L Year 3
  - Differentiator: 3 research papers + 1 production system + 30-founder cohort
  - Success metric: 500K MAU on www.viadecide.com by Month 12

**Task 1.2: Digital Twin Architecture Specification**
- File: `DIGITAL_TWIN_ARCHITECTURE.md`
- Output: Technical spec document
- Sections:
  - Platform choice: NVIDIA Omniverse vs CARLA (recommend CARLA for cost/simplicity)
  - Kutch highway simulation: 20km section, 1M vehicle passages/hour, 20–48°C thermal dynamics
  - Data pipeline: Tire pressure → anomaly detection → drift monitoring
  - Integration points: Jetson Orin hardware, cloud backend (Firebase/GCP), monitoring (Evidently AI)
  - Validation: Benchmark against real NHAI data (Phase 2b)

**Task 1.3: Stakeholder Narratives (3 documents)**
- Files: `STAKEHOLDER_NARRATIVES.md` (unified) or split into:
  - `NARRATIVE_NHAI.md` — Highway safety + cost reduction + pilot site
  - `NARRATIVE_INVESTORS.md` — ₹1Cr capital → ₹100L Year 1 revenue → ₹500L+ Year 3
  - `NARRATIVE_RESEARCHERS.md` — 3 papers, 1K+ citations, AAAI/NeurIPS venues, open dataset
- Each 800–1000 words, brand-aligned, outcome-focused

**Task 1.4: "Why Kutch?" Narrative**
- File: `WHY_KUTCH.md`
- Output: 600 words
- Points:
  - Extreme climate (20–48°C) = first-ever ML system tested at scale
  - Highway corridor (NHAI) = 1M vehicle passages/hour = real-world data volume
  - Deendayal Port + logistics hub = downstream applications ready
  - Geographic advantage = isolation = controlled experiment + media narrative

---

## PROMPT 2: kup-research
### Executive Brief
Define 3 research papers, 1 Hugging Face dataset, and benchmark suite. Output: Research roadmap, dataset schema, baseline models, venue targets.

### Directory Structure
```
kup-research/
├── README.md
├── PAPER_1_DATA_DRIFT.md
├── PAPER_2_KUTCH_TIRE_ANOMALY_DATASET.md
├── PAPER_3_DATA_CENTRIC_AI.md
├── DATASET_SCHEMA.json
├── BENCHMARK_SUITE.md
├── BASELINE_MODELS.py
├── PUBLICATION_ROADMAP.md
└── citations-tracker.json
```

### Tasks (Sequential)

**Task 2.1: Paper 1 — Data Drift in Extreme Climates**
- File: `PAPER_1_DATA_DRIFT.md`
- Outline (can be expanded to full draft):
  - Abstract: Model accuracy degradation across 20–48°C on tire pressure sensors
  - Methods: 6 data quality dimensions (missing values, noise, drift, seasonality, outliers, class imbalance)
  - Dataset: 500K vehicle passages from Kutch NHAI corridor
  - Results: 3 drift mitigation strategies (retraining cadence, active learning, data augmentation)
  - Impact: First-ever ML system tested in Kutch-extreme climate
  - Venues: AAAI, NeurIPS, ICML (target 1st submission Month 6)

**Task 2.2: Dataset Definition — KUTCH-TIRE-ANOMALY (KTA)**
- File: `DATASET_SCHEMA.json`
- Output: Complete JSON schema
- Fields:
  - vehicle_id, timestamp, tire_pressure (4 tires), temperature, humidity, altitude, speed, road_condition, anomaly_label (0/1), severity (0-10)
  - 1M records, 500K unique vehicles, 12 months continuous
  - Splits: 70% train, 10% validation, 20% test (time-stratified)
  - License: CC-BY-4.0 (open research)
- Hugging Face dataset name: `via-decide/kutch-tire-anomaly`
- Upload schedule: Month 4 (after NHAI pilot data collected)

**Task 2.3: Paper 2 — KUTCH-TIRE-ANOMALY Dataset Paper**
- File: `PAPER_2_KUTCH_TIRE_ANOMALY_DATASET.md`
- Sections:
  - Dataset motivation: Why Kutch is unique (extreme climate + scale)
  - Collection methodology: NHAI partnership, data governance, privacy compliance
  - Benchmark tasks: Anomaly detection, drift detection, forecasting
  - Baseline results: 5 models (random forest, XGBoost, LSTM, Transformer, custom CNN)
  - Community impact: Enable research on climate resilience
  - Venue: IEEE TODS or NeurIPS Datasets & Benchmarks track

**Task 2.4: Paper 3 — Data-Centric AI in Physical Infrastructure**
- File: `PAPER_3_DATA_CENTRIC_AI.md`
- Outline:
  - Argument: Model-centric AI fails on noisy, drifting real-world data. Data-centric approach wins.
  - Evidence: Clean data (KTA curated) > complex model (in Scenario 2 simulation)
  - Methods: Data quality pipeline, curation workflow, active learning loop
  - Results: 85%+ accuracy on noisy data with simple model vs 60% with complex model on raw data
  - Application: TPM, other IoT/sensor systems
  - Venue: IEEE Transactions on Industrial Informatics or ACM Trans. Intelligent Systems

**Task 2.5: Benchmark Suite & Baseline Models**
- File: `BENCHMARK_SUITE.md`
- Output: 5 benchmark tasks with evaluation metrics
  - Task 1: Tire pressure anomaly detection (AUC-ROC, F1)
  - Task 2: Drift detection (time-series; detection delay, false positives)
  - Task 3: 24-hour pressure forecasting (MAE, RMSE)
  - Task 4: Vehicle classification by anomaly severity (accuracy, confusion matrix)
  - Task 5: Cross-climate generalization (train on Kutch, test on synthetic Scenario 3)
- File: `BASELINE_MODELS.py` — 5 starter implementations (scikit-learn, PyTorch, TensorFlow)

**Task 2.6: Publication Roadmap**
- File: `PUBLICATION_ROADMAP.md`
- Timeline:
  - Month 3: Paper 1 (Data Drift) draft → Month 5 submission
  - Month 4: Dataset paper → Month 6 submission
  - Month 7: Paper 3 (Data-Centric AI) → Month 9 submission
  - Target: 1K+ citations by Month 18 (calculated backward from venue impact factors)

---

## PROMPT 3: kup-curriculum
### Executive Brief
Integrate Month 1 4-week curriculum with digital twin. Define Year 1 52-week roadmap for www.viadecide.com (37 tools, 500K MAU). Output: Syllabus, weekly deliverables, KPI dashboard.

### Directory Structure
```
kup-curriculum/
├── README.md
├── MONTH_1_SYLLABUS.md
├── MONTH_1_WEEK_1.md
├── MONTH_1_WEEK_2.md
├── MONTH_1_WEEK_3.md
├── MONTH_1_WEEK_4.md
├── YEAR_1_ROADMAP.md
├── SKILLS_MATRIX.json
├── COHORT_STRUCTURE.md
├── TOOLS_ONBOARDING.md
└── kup-curriculum-tracker.jsx
```

### Tasks (Sequential)

**Task 3.1: Month 1 Syllabus (4 weeks)**
- File: `MONTH_1_SYLLABUS.md`
- Overview: Data-centric AI for TPM (Tire Pressure Monitoring)
- Prerequisites: Python 3.8+, Jupyter, git
- Learning outcomes: Data quality fundamentals, digital twin basics, decision trees (ViaLogic)
- Tools: ViaLogic (Week 1), Prompt Alchemy (Week 2), Script Writer (Week 3), Hook Writer + Caption Generator (Week 4)

**Task 3.2: Weekly Breakdowns (MONTH_1_WEEK_*.md)**
- **Week 1:** Problem definition + Data quality charter
  - Deliverable: Use-case charter signed, ViaLogic decision tree mapped
  - Live tool: ViaLogic (interactive decision tree builder)
  - Metric: Charter completion
  
- **Week 2:** Simulated pipelines + 500K vehicle passages
  - Deliverable: End-to-end data pipeline, 20% noise injection test
  - Live tool: Prompt Alchemy (LLM prompt chains for data validation)
  - Metric: Pipeline accuracy >80%
  
- **Week 3:** Edge deployment on Jetson Orin
  - Deliverable: Sub-50ms inference, drift detection live
  - Live tool: Script Writer (code generation for edge inference)
  - Metric: Accuracy stability >85%
  
- **Week 4:** MVP completion + Demo day
  - Deliverable: Working TPM system, docs, investor pitches
  - Live tools: Hook Writer + Caption Generator (pitch narrative + visuals)
  - Metric: MVP delivery, 3+ investor conversations

**Task 3.3: Year 1 Roadmap (52 weeks, 37 tools, 500K MAU)**
- File: `YEAR_1_ROADMAP.md`
- Structure:
  - Months 1–2: Shell UI, nav-registry.json, router.js, landing page, 50K users
  - Months 3–4: All 37 tools migrated, beta launch, 150K users
  - Months 5–6: Cross-tool state sharing, performance optimization, 300K users
  - Months 7–9: Data infrastructure, user research, analytics, 400K users
  - Months 10–12: Polish, 500K MAU target, Year 2 planning
- Dependencies: Vertical teams (Core Tools, Games, Productivity, Education+Experiments)
- Success criteria: All tools at /tool/{id}, zero broken links, <2s load, 99.5% uptime, 500K MAU

**Task 3.4: Skills Matrix**
- File: `SKILLS_MATRIX.json`
- 4 roles: Infrastructure (2), Data Pipeline (2), Product+Ops (2)
- Skills per role: Technical depth, leadership, domain (KUP/Kutch), ViaDecide tooling
- Progression: Month 1 (foundational) → Month 3 (intermediate) → Month 6 (advanced) → Month 12 (expert)

**Task 3.5: Cohort Structure**
- File: `COHORT_STRUCTURE.md`
- 30 co-founders, 5 phase teams, 4 vertical teams
- Phase teams: Shell (Wk1-4), Migration (Wk5-12), Cross-tool (Wk13-18), Polish (Wk19-20), Deploy (Wk21-24)
- Vertical teams: Core Tools (6), Games (6), Productivity (6), Education+Experiments (6), Domain teams (6): IoT+Hardware, Finance+Metrics, Design+UX, Sales+Marketing

**Task 3.6: Tools Onboarding**
- File: `TOOLS_ONBOARDING.md`
- For each of 37 tools: 1-page onboarding (name, category, live demo link, integration checklist, dependencies)
- Tools reference: decide.engine-tools (44 tools total, 5 integrated into VIA)

---

## PROMPT 4: kup-program
### Executive Brief
Build ruthless execution framework: Sprint schedule, mentor matching, KPI dashboard, 3 founder outcome paths, stakeholder comms templates, failure tolerance ceiling. Output: Program ops playbook.

### Directory Structure
```
kup-program/
├── README.md
├── SPRINT_SCHEDULE.md
├── MENTOR_FRAMEWORK.md
├── ENERGY_MANAGEMENT.md
├── FAILURE_TOLERANCE_CEILING.md
├── KPI_DASHBOARD.md
├── POST_MONTH_1_ROADMAP.md
├── FOUNDER_MATCHING_FRAMEWORK.md
├── THREE_OUTCOME_PATHS.md
├── STAKEHOLDER_COMMS_TEMPLATES.md
├── CONTINGENCY_PLANS.md
└── kup-program-dashboard.jsx
```

### Tasks (Sequential)

**Task 4.1: Ruthless Sprint Schedule**
- File: `SPRINT_SCHEDULE.md`
- Structure: 24 weeks (Month 1–6) with bi-weekly sprints
- Week 1–4: Shell + Router + Landing (hard dependency for all teams)
- Week 5–12: 37 tools migrated in parallel (4 teams working simultaneously)
- Week 13–18: Cross-tool integration, state sharing, performance optimization
- Week 19–20: UI/UX polish, accessibility audit
- Week 21–24: Hardening, deployment, post-launch support
- Standups: Daily (async Slack + 3x weekly live), sprint reviews Fridays
- Failure point: Any team 3+ days behind → immediate escalation to Via

**Task 4.2: Mentor Framework**
- File: `MENTOR_FRAMEWORK.md`
- 30 co-founders → 30 mentors (1:1 matching)
- Mentor responsibilities: Weekly 1:1, unblock technical/business blockers, accountability
- Mentor network: Engineers (10), PMs (5), Data scientists (5), Business operators (5), Design leads (5)
- Mentor onboarding: 2-hour session covering goals, 3 outcome paths, KPI dashboard, failure tolerance ceiling
- Escalation path: Mentor → Phase lead → Via (via.decide@gmail.com)

**Task 4.3: Energy Management & Failure Tolerance**
- File: `ENERGY_MANAGEMENT.md`
- Work cadence: 6 AM–12 AM (18-hour window) strict; no all-nighters
- Recovery: Mandatory 2-day break every 3 weeks
- Mental health: Weekly check-ins, burnout assessment, sabbatical options (1 week / month)
- File: `FAILURE_TOLERANCE_CEILING.md`
- Hard ceiling: 2 consecutive sprint failures (missed KPI) → role re-evaluation
- Soft failures: 1 sprint miss → mentor + lead support, public post-mortem, learning doc

**Task 4.4: KPI Dashboard**
- File: `KPI_DASHBOARD.md` (text spec for dashboard)
- Metrics (tracked weekly):
  - Build progress: Tools migrated (target 37 by Week 12), links broken (target 0), load time (target <2s)
  - Team health: Sprint velocity (target 80+ points), PR review time (target <24h), mentor engagement (target 100%)
  - Business: MAU (target 50K → 500K), retention rate (target >60%), daily active users
  - Research: Paper submissions (3 by Month 7), dataset downloads (1K+ by Month 6), citations (target 100+ by Month 9)
- Dashboard tool: Create `kup-program-dashboard.jsx` (React component, live data from Firestore)

**Task 4.5: Post-Month-1 Roadmap (Months 2–12)**
- File: `POST_MONTH_1_ROADMAP.md`
- Month 2–3: All 37 tools live, user onboarding, VC outreach
- Month 4–6: Cross-tool features, 3 papers submitted, NHAI pilot site secured
- Month 7–9: Analytics, monetization model, 2nd cohort (40 co-founders)
- Month 10–12: 500K MAU, revenue targets (₹100L Y1), Year 2 product roadmap

**Task 4.6: Founder Matching Framework**
- File: `FOUNDER_MATCHING_FRAMEWORK.md`
- 30 co-founders, 3 outcome paths
- Infrastructure Startup (10): Senior engineers, logistics/hardware background, business acumen
- Research Venture (10): ML PhDs, academic networks, publications track record
- Edge AI Platform (10): Full-stack engineers, SaaS experience, customer discovery skills
- Matching algorithm: Skills inventory → path compatibility score → manual refinement

**Task 4.7: Three Outcome Paths (Detailed)**
- File: `THREE_OUTCOME_PATHS.md`
- **Path 1: Infrastructure Startup** (TPM for highways + logistics)
  - Team: 10 engineers
  - Year 1 goal: ₹10+ crore revenue, 1+ highway pilot live
  - Exit: Acquisition by logistics company or IPO
  - Deliverables: Working pilot, cost-per-lane quantified, NHAI partnership formalized
  
- **Path 2: Research Venture** (Open datasets + papers)
  - Team: 10 ML scientists
  - Year 1 goal: 3 papers, 1K+ citations, 5+ research collaborations
  - Exit: Research institute, academia advisory, government labs
  - Deliverables: 3 papers, KTA dataset 1K+ downloads, thought leadership
  
- **Path 3: Edge AI Platform** (SaaS for distributed ML)
  - Team: 10 full-stack engineers
  - Year 1 goal: 20+ customers, $50K+ MRR
  - Exit: Acquisition, IPO, or sustainable standalone business
  - Deliverables: Jetson-optimized toolkit, SaaS MVP, 1K+ GitHub stars

**Task 4.8: Stakeholder Comms Templates**
- File: `STAKEHOLDER_COMMS_TEMPLATES.md`
- Email templates for:
  - Weekly investor updates (1 template)
  - NHAI partnership checkpoint (1 template)
  - Mentor check-ins (1 template)
  - Founder feedback loops (1 template)
  - Research paper submissions (1 template)
  - Press announcements (2 templates: Month 1 launch, Month 6 milestone)

**Task 4.9: Contingency Plans**
- File: `CONTINGENCY_PLANS.md`
- Scenario 1: NHAI delays pilot site
  - Mitigation: Synthetic CARLA simulation escalated to production, partnerships with truck fleets for data
- Scenario 2: Key team member departs
  - Mitigation: Cross-training, mentor escalation, role backfill from external network
- Scenario 3: Research paper rejections
  - Mitigation: Venue pivot strategy, preprint circulation, open-source dataset release

---

## PROMPT 5: kup-ai-stack
### Executive Brief
Build layered AI architecture (Edge→Streaming→ML→Storage→API→Interface), deployment guides (Jetson Orin, cloud backend, monitoring), and reference architecture publication.

### Directory Structure
```
kup-ai-stack/
├── README.md
├── ARCHITECTURE_DIAGRAM.md
├── EDGE_LAYER.md
├── STREAMING_LAYER.md
├── ML_LAYER.md
├── STORAGE_LAYER.md
├── API_LAYER.md
├── INTERFACE_LAYER.md
├── DEPLOYMENT_GUIDE_JETSON.md
├── DEPLOYMENT_GUIDE_CLOUD.md
├── MONITORING_OBSERVABILITY.md
├── CI_CD_PIPELINE.md
├── REFERENCE_ARCHITECTURE.md
├── architecture-diagram.svg
└── system-design.json
```

### Tasks (Sequential)

**Task 5.1: Layered Architecture Overview**
- File: `ARCHITECTURE_DIAGRAM.md`
- Layers (top-to-bottom):
  1. **Interface:** React dashboard + ViaDecide tools (decide.engine)
  2. **API:** REST + WebSocket (Node.js, Firebase)
  3. **Storage:** Firestore (primary), BigQuery (analytics), GCS (models)
  4. **ML:** TensorFlow + PyTorch models, Jetson Orin edge inference
  5. **Streaming:** Apache Kafka / Pub/Sub (real-time data pipeline)
  6. **Edge:** Jetson Orin Nano (sub-50ms inference, local caching)
- Diagram: Create `architecture-diagram.svg` (Lucidchart or similar)
- Data flow: Tire pressure sensor → Jetson → Kafka → ML models → API → UI

**Task 5.2: Edge Layer (Jetson Orin)**
- File: `EDGE_LAYER.md`
- Hardware: NVIDIA Jetson Orin Nano ($100, 8GB RAM)
- Software stack: TensorRT (inference), NVIDIA NVMe (local storage)
- Models: Quantized TensorFlow models (FP16/INT8), <50ms inference
- Local intelligence: Anomaly detection, drift monitoring, caching
- Failover: Local decision trees if network unavailable

**Task 5.3: Streaming Layer**
- File: `STREAMING_LAYER.md`
- Options: Google Pub/Sub (managed) vs Apache Kafka (self-hosted)
- Recommendation: Pub/Sub for MVP (Month 1–2), Kafka for scale (Month 6+)
- Message schema: JSON, tire_pressure + timestamp + vehicle_id
- Throughput target: 1M messages/hour (scalable to 10M)
- Retention: 7 days hot, 30 days archive

**Task 5.4: ML Layer**
- File: `ML_LAYER.md`
- Models:
  - Anomaly detection: Isolation Forest (baseline) + LSTM (production)
  - Drift detection: Evidently AI + custom statistical tests
  - Forecasting: Prophet + Transformer (optional)
- Model registry: TensorFlow Hub + HuggingFace
- Serving: TensorFlow Serving + Seldon Core (Kubernetes)
- A/B testing: Shadow mode (Month 2–3), canary (Month 4+)

**Task 5.5: Storage Layer**
- File: `STORAGE_LAYER.md`
- Firestore: Real-time vehicle state, sensor readings, alerts
- BigQuery: Historical analysis, research queries, ML training data
- Cloud Storage: Model artifacts, training datasets, backups
- Data governance: PII redaction, audit logging, access control

**Task 5.6: API Layer**
- File: `API_LAYER.md`
- Endpoints:
  - `/api/vehicles/{id}/pressure` (GET/POST)
  - `/api/anomalies` (GET, real-time stream)
  - `/api/predictions/{vehicle_id}` (GET, next 24h forecast)
  - `/api/models/status` (GET, model health)
- Authentication: API keys (Jetson) + OAuth2 (web)
- Rate limiting: 1K requests/min per Jetson, 10K/min per user

**Task 5.7: Interface Layer**
- File: `INTERFACE_LAYER.md`
- Frontend: React (ViaDecide dashboard)
- Real-time: WebSocket connections (live alerts, vehicle map)
- Tools integration: ViaLogic (decision trees), PromptAlchemy (model performance analysis)
- Offline support: Service Worker, local IndexedDB

**Task 5.8: Deployment Guide — Jetson Orin**
- File: `DEPLOYMENT_GUIDE_JETSON.md`
- Steps:
  1. Flash Jetson OS (JetPack 6.0)
  2. Install TensorRT, CUDA 12.2
  3. Pull Docker image: `ghcr.io/via-decide/tpm-edge:latest`
  4. Configure Pub/Sub auth (service account key)
  5. Verify sub-50ms inference
  6. Test failover (offline mode)
- Success criteria: Model.infer() < 50ms, 99.9% uptime, zero network errors

**Task 5.9: Deployment Guide — Cloud Backend**
- File: `DEPLOYMENT_GUIDE_CLOUD.md`
- Infrastructure: Google Cloud Run (stateless APIs), Cloud Functions (triggers)
- Database: Firestore multi-region replication (us-central1, asia-south1)
- ML serving: Vertex AI + TensorFlow Serving
- Monitoring: Cloud Trace, Cloud Logging, Cloud Monitoring
- Cost optimization: Autoscaling (0–100 instances), pre-emptible VMs

**Task 5.10: Monitoring & Observability**
- File: `MONITORING_OBSERVABILITY.md`
- Metrics: Inference latency, model accuracy, data quality, API error rate
- Dashboards: Grafana + Cloud Monitoring
- Alerts: PagerDuty (P0: accuracy drop >5%, P1: inference latency >100ms)
- Logging: Structured logs (JSON), centralized in BigQuery

**Task 5.11: CI/CD Pipeline**
- File: `CI_CD_PIPELINE.md`
- Tool: GitHub Actions
- Stages: Build → Test → Quality gates → Deploy (staging) → Deploy (production)
- Quality gates: Unit test coverage >80%, type checking (mypy), linting (pylint)
- Deployment: Canary (5% traffic) → Progressive rollout (100% over 4 hours)

**Task 5.12: Reference Architecture Publication**
- File: `REFERENCE_ARCHITECTURE.md`
- Target audience: ML engineers building production systems
- Sections:
  - Problem statement (data quality, drift, edge inference)
  - Architecture overview (diagram + narrative)
  - Technology choices & trade-offs
  - Lessons learned (cost, scalability, failure modes)
  - Benchmarks (inference latency, throughput, cost per inference)
- Publication venue: Towards Data Science, Medium, or IEEE IoT Magazine

---

## PROMPT 6: kup-partnerships
### Executive Brief
Build partnership strategy for NHAI, Deendayal Port, NVIDIA, Kistler, AWS/GCP. Output: Outreach emails, MOUs, value props, 3-month roadmaps per partner.

### Directory Structure
```
kup-partnerships/
├── README.md
├── PARTNERSHIP_STRATEGY.md
├── PARTNER_PROFILES.md
├── NHAI_ENGAGEMENT_PLAN.md
├── DEENDAYAL_PORT_ENGAGEMENT.md
├── NVIDIA_PARTNERSHIP.md
├── KISTLER_PARTNERSHIP.md
├── CLOUD_PARTNERSHIP.md
├── OUTREACH_EMAIL_TEMPLATES.md
├── MOU_TEMPLATES.md
├── VALUE_PROPOSITIONS.md
├── 3MONTH_ROADMAPS.md
├── partnership-tracker.jsx
└── stakeholder-matrix.json
```

### Tasks (Sequential)

**Task 6.1: Partnership Strategy Overview**
- File: `PARTNERSHIP_STRATEGY.md`
- Goal: 5 strategic partnerships by Month 6 → ecosystem for scale by Month 12
- Partners:
  - NHAI: Highway pilot site, real data, regulatory pathway
  - Deendayal Port: Logistics pilot, fleet data, port operations insights
  - NVIDIA: Hardware (Jetson), joint marketing, TensorRT optimization
  - Kistler (tire sensors): Hardware integration, calibration, sensor data quality
  - AWS/GCP: Cloud infrastructure, ML services, joint go-to-market
- Expected outcomes: 1 pilot site live, 3 research collaborations, 10K+ MAU from ecosystem

**Task 6.2: Partner Profiles**
- File: `PARTNER_PROFILES.md`
- For each partner: Current state → Mutual gains → Decision-maker → Timeline
- Format: 300 words per partner

**Task 6.3: NHAI Engagement Plan**
- File: `NHAI_ENGAGEMENT_PLAN.md`
- Objectives:
  - Pilot site: 1 km highway (20–30 vehicles), 3-month trial, cost-per-vehicle quantified
  - Real data: 500K vehicle passages for KTA dataset
  - Regulatory pathway: Safety impact, liability framework
- Timeline:
  - Month 1: Decision-maker identification + intro call
  - Month 2: Technical presentation + site survey
  - Month 3: MOA signed + equipment deployment
  - Month 4: Data collection begins
  - Month 6: Results & scale discussion
- Success metric: 1 km pilot live, NHAI letter of intent for Year 2 expansion

**Task 6.4: Deendayal Port Engagement**
- File: `DEENDAYAL_PORT_ENGAGEMENT.md`
- Objectives:
  - Logistics pilot: Fleet of 50 vehicles, port operations monitoring
  - Supply chain resilience: Real-time vehicle health monitoring
  - Data share: Port operational data (weather, congestion, port schedules)
- Timeline: Month 2 intro → Month 5 pilot → Month 9 scale
- Value prop: 2% fuel cost reduction, predictive maintenance (10% downtime reduction)

**Task 6.5: NVIDIA Partnership**
- File: `NVIDIA_PARTNERSHIP.md`
- Objectives:
  - Hardware: 100 Jetson Orin Nano units for Month 4 deployment
  - Software: TensorRT optimization, NVIDIA developer program
  - Marketing: Joint use case, NVIDIA blog post, developer documentation
  - Funding: Potential co-investment (₹50L for scale)
- Timeline: Month 1 intro → Month 3 hardware pledge → Month 6 marketing launch
- Success metric: 100 Jetson units deployed, NVIDIA case study published

**Task 6.6: Kistler Sensor Partnership**
- File: `KISTLER_PARTNERSHIP.md`
- Objectives:
  - Hardware: Tire pressure sensors (100 units) + technical support
  - Calibration: Sensor accuracy benchmarking, thermal compensation
  - Integration: Custom firmware for edge data collection
  - Research: Joint white paper on tire sensor reliability in extreme climate
- Timeline: Month 1 intro → Month 3 pilot deployment → Month 6 white paper
- Value prop: Kistler reaches new market (IoT/edge), KUP gets validated sensors

**Task 6.7: Cloud Partnership (AWS/GCP)**
- File: `CLOUD_PARTNERSHIP.md`
- Objectives:
  - Infrastructure credits: ₹50L+ for Year 1 cloud costs
  - ML services: Vertex AI / SageMaker integration
  - Joint GTM: API marketplace, reference architecture on AWS/GCP blogs
  - Funding: Startup grant program (₹20–30L possible)
- Timeline: Month 1 intro → Month 3 credits → Month 6 API integration → Month 9 GTM campaign
- Success metric: Full infrastructure on AWS/GCP, 10M+ API calls/month, co-marketing launch

**Task 6.8: Outreach Email Templates**
- File: `OUTREACH_EMAIL_TEMPLATES.md`
- Templates:
  1. Cold intro (C-level) — "Highway safety in extreme climates"
  2. Technical deep-dive (engineering lead) — "Real-world ML validation for tire pressure"
  3. Partnership proposal (business dev) — "Pilot timeline + commercial model"
  4. Follow-up sequences (3 emails, 5-day cadence)
- Personalization: Decision-maker name, company pain point, specific mutual gain

**Task 6.9: MOU & LOI Templates**
- File: `MOU_TEMPLATES.md`
- Sections:
  - Partnership objectives (pilot site, data share, research)
  - Timeline (3–6 months)
  - Investment/resource commitment (hardware, infrastructure, team time)
  - IP ownership (open dataset CC-BY-4.0, proprietary models in escrow)
  - Success metrics & escalation path
- Format: 2–3 page template, editable per partner

**Task 6.10: Value Propositions (Per Partner)**
- File: `VALUE_PROPOSITIONS.md`
- NHAI: "Real-time tire health monitoring → 2% fuel cost reduction, safety compliance, data for 3 publications"
- Deendayal Port: "Fleet predictive maintenance → 10% uptime improvement, supply chain resilience, competitive advantage"
- NVIDIA: "New edge use case for Jetson → case study, developer community, ₹100L+ customer LTV potential"
- Kistler: "Extreme climate validation for sensors → new market entry, co-marketing, 10K+ units potential"
- AWS/GCP: "Data-centric AI framework → go-to-market differentiation, enterprise customer pipeline"

**Task 6.11: 3-Month Roadmaps (Per Partner)**
- File: `3MONTH_ROADMAPS.md`
- Month 1: Discovery + relationship building
  - Calls scheduled, decision-makers mapped, technical POC assigned
- Month 2: Pilot design + resource commitment
  - Site survey (NHAI), hardware spec (NVIDIA/Kistler), credits agreed (AWS/GCP)
- Month 3: Execution kickoff
  - Equipment deployment, data sharing agreements, joint technical team formed
- Win metrics: Signed MOU, pilot site secured, hardware commitment confirmed, credits unlocked

**Task 6.12: Partnership Tracker Dashboard**
- File: `partnership-tracker.jsx`
- React component displaying:
  - 5-stage pipeline: Prospecting → Decision → Commitment → Deployment → Scale
  - Partner status: Timeline on track / at risk / completed
  - Metrics: Hardware units deployed, data volume collected, research outputs, revenue impact
  - Alerts: Escalation needed (timeline slipping)

---

## EXECUTION NOTES

### Prerequisites for All Prompts
- GitHub repos cloned locally
- Git config: `user.email = via.decide@gmail.com`, `user.name = Via`
- GitHub token available for pushes
- Telegram bot ready for async status updates

### Delivery Format
- All outputs as markdown (.md) or JSON (.json) or React components (.jsx)
- Commit + push to appropriate GitHub repo per prompt
- Tag commits with `#claude-code`, `#month-1`, `#kup-program` etc.
- Post status to Telegram (format: "✅ kup-ai-systems-lab: BRAND_POSITIONING.md complete" or "⚠️ kup-research: Paper 1 draft needs review")

### Timeline
- **Total effort:** 40–50 hours (5–7 days at 8 hours/day)
- **Ideal sequence:** Run prompts in parallel where possible
  - Prompt 1 (ai-systems-lab) → supports Prompt 2 (research) positioning
  - Prompt 3 (curriculum) + Prompt 4 (program) → interdependent (sync weekly)
  - Prompt 5 (ai-stack) → technical backbone (run after Prompt 1 scoping)
  - Prompt 6 (partnerships) → independent, can run in parallel

### Success Criteria
- [ ] All 6 repos have README + core documents
- [ ] 3 research papers outlined (+ 1 full draft if time)
- [ ] 37 tools onboarded + www.viadecide.com curriculum mapped
- [ ] 30 co-founders + 3 outcome paths defined + KPI dashboard live
- [ ] Architecture diagram + deployment guides complete
- [ ] 5 partnership MOUs drafted + outreach emails ready
- [ ] Zero broken links, all documents in GitHub, main branch clean

---

**Next: Update kup-visual-overview.jsx for mobile UI responsiveness (60-min task)**
