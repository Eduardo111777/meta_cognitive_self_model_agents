
# 🤖 Neural-Augmented Self-Modeling Agents

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

A modular framework for building Self-Modeling Agents with explicit internal state representation and adaptive cognitive control, as described in:

> Mozo, H. E. (2025). Neural-Augmented Self-Modeling Agents: Design, Implementation, and Evaluation of a Modular Approach to Meta-Cognitive Artificial Intelligence. *Journal of Artificial Intelligence Research (JAIR)*, Vol. 83, Article X. https://jair.org/

---

## 🚀 Project Overview

This framework enables agents to dynamically model and adapt their confidence, fatigue, and behavioral mode via dedicated neural sub-models. It supports:

- Single-agent & multi-agent execution
- Meta-learner driven analysis & adaptation
- Full scientific metrics pipeline & visualization
- Modular architecture for extensibility & reproducibility

---

## 🗂️ Project Architecture

The framework is fully modular, extensible, and aligned with scientific reproducibility standards.

```
SELF_MODEL_AGENTS/
├── docs/
│   ├── meta_learner_memory/
│   ├── meta_learner_reports/
│   └── meta_learner_system/
├── outputs/
│   ├── logs/
│   ├── metrics/
│   ├── models/
│   ├── scientific_metrics/
│   ├── self_model_logs/
│   ├── self_model_weights/
│   └── visualizations/
├── scripts/
│   ├── run_gridworld_experiment.py
│   ├── run_multi_agent_experiment.py
│   ├── visualize_multi_agent.py
│   └── visualize_self_model.py
├── self_model_agents/
│   ├── policy/
│   ├── self_model/
│   ├── utils/
│   ├── agent.py
├── gui_main.py
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

### Main Framework Modules

- **Meta-Learner System (`meta_learner_system/`)**: 
  - Meta-cognitive layer monitoring agent dynamics.
  - Predictive models of confidence, fatigue, mode switching.
  - Scientific metrics & visualizations.

- **Self-Model Agents (`self_model_agents/`)**:
  - SelfModel components (Simple / Advanced).
  - Policy modules with varying meta-cognitive adaptation.
  - Agent-environment interaction loop.

- **Experiment Runners (`scripts/`)**:
  - Single-agent & multi-agent pipelines.
  - Visualization tools.

- **Outputs (`outputs/`)**:
  - Logs & scientific reports.
  - Publication-ready visualizations.

---

## 📊 Key Features

- Meta-learner driven adaptive agents
- Modular SelfModel & Policy design
- Multi-agent execution & coordination
- Reproducible scientific metrics
- Visualization dashboards

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/self_model_agents.git
cd self_model_agents
pip install -r requirements.txt
```

---

## 🚀 Running Experiments

### Single-Agent Experiment

```bash
python scripts/run_gridworld_experiment.py
```

### Multi-Agent Experiment

```bash
python scripts/run_multi_agent_experiment.py
```

### Visualizations

```bash
python scripts/visualize_self_model.py
python scripts/visualize_multi_agent.py
```

---

## 🤝 Contribution

We welcome contributions!

1. Fork the repository
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow the existing coding style and include tests for new functionality.

---

## 📜 License

This project is licensed under the **Apache 2.0 License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

This framework was developed as part of:

> Mozo, H. E. (2025). Neural-Augmented Self-Modeling Agents: Design, Implementation, and Evaluation of a Modular Approach to Meta-Cognitive Artificial Intelligence. *JAIR*, Vol. 83.

If you use this framework in academic work, please cite the paper. 📚

---
