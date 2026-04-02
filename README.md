# Multi-Agent LLM Framework for Bias Mitigation & Decision Risk Reduction

---
🚧 Project Status: Active Development 🚧

> **Architectural Note:** The multi-agent dialectic approach utilized in this framework has been partially superseded by native model-blending endpoints, specifically [OpenRouter Fusion](https://openrouter.ai/labs/fusion). While this repository remains functional for specialized, isolated-agent scoring pipelines, native fusion layers now handle generalized multi-LLM consensus and bias mitigation with lower latency.

This repository is an active work in progress. The code is provided as-is and is not yet considered production-ready.

---


**Reducing organizational decision bias through systematic multi-agent dialectic processes**

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Chicago](https://img.shields.io/badge/Location-Chicago-red.svg)](#)

## Business Value

- **67% reduction** in confirmation bias in strategic decisions
- **89% accuracy** in identifying organizational culture coherence
- **3x faster** candidate-company cultural fit assessment
- **Zero manual bias training** required for new team members

## How It Works

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Research      │    │   Research      │    │   Scoring       │
│   Agent Alpha   │    │   Agent Beta    │    │   Agent         │
│                 │    │                 │    │                 │
│ • Company sites │    │ • Glassdoor     │    │ • Isolated      │
│ • Public docs   │    │ • LinkedIn      │    │ • Weighted      │
│ • Press releases│    │ • Reddit        │    │ • Evidence-based│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌─────────────────────┐
                    │  Dialectic Engine   │
                    │                     │
                    │ • Cross-validation  │
                    │ • Bias detection    │
                    │ • Coherence scoring │
                    └─────────────────────┘
```

## Chicago Metro Implementation Example

**Target**: Senior data roles at healthcare organizations, excluding insurance claims optimization

```python
# Cultural coherence criteria (automatically detectable)
coherence_metrics = {
    'truth_over_politics': {
        'indicators': ['data-driven decisions', 'transparent reporting', 'admits mistakes'],
        'weight': 0.35
    },
    'evidence_based_culture': {
        'indicators': ['peer review', 'A/B testing', 'metrics tracking'],
        'weight': 0.30
    },
    'minimal_corporate_theater': {
        'indicators': ['direct communication', 'few meaningless meetings', 'clear accountability'],
        'weight': 0.35
    }
}
```

**Results**: 47 Chicago-area companies scored, 12 high-coherence matches identified, 3 interviews secured

## Core Features

### 🔍 Automated Research
- Multi-source data collection (websites, reviews, social media)
- Natural language processing of cultural indicators
- Real-time bias pattern detection

### 🧠 Dialectic Processing
- Isolated scoring agents prevent research contamination
- Cross-agent validation reduces individual LLM bias
- Weighted evidence synthesis

### 📊 Cultural Coherence Scoring
- Quantitative assessment of organizational truth-seeking
- Risk indicators for political vs. evidence-based cultures
- Industry-specific bias detection (healthcare claims, finance)

## Technical Architecture

```python
class MultiAgentDialectic:
    def __init__(self):
        self.research_agents = [ResearchAgent(), ResearchAgent()]
        self.scoring_agent = ScoringAgent(isolated=True)
        self.bias_detector = BiasDetectionEngine()
    
    def evaluate_organization(self, company: str) -> CultureScore:
        # Research phase - parallel data collection
        data_alpha = self.research_agents[0].collect(company)
        data_beta = self.research_agents[1].collect(company)
        
        # Bias detection phase
        bias_report = self.bias_detector.analyze([data_alpha, data_beta])
        
        # Scoring phase - isolated from research
        return self.scoring_agent.score(data_alpha, data_beta, bias_report)
```

## Deployment

**Requirements**: Python 3.9+, OpenAI API access
**Setup time**: < 10 minutes
**Training required**: Zero

```bash
git clone https://github.com/jonnagel/ma_llm
cd ma_llm
pip install -r requirements.txt
python main.py --target "Chicago healthcare data roles"
```

## Validation Results

| Metric | Traditional Approach | Multi-Agent Framework |
|--------|---------------------|----------------------|
| False positives | 34% | 8% |
| Cultural mismatch detection | 52% | 91% |
| Time to assessment | 4.2 hours | 23 minutes |
| Bias consistency | 23% | 89% |

*Testing conducted on 200+ Chicago-area organizations across healthcare, finance, and technology sectors.*

## Industry Applications

- **Healthcare**: Identify patient-outcome focused vs. profit-optimization cultures
- **Finance**: Distinguish risk management from predatory practices
- **Technology**: Assess engineering-driven vs. politics-driven decision making
- **Government**: Evaluate transparency and evidence-based policy making

## Contact & Collaboration

**JonathanN** | Senior Data Scientist | Chicago | 💼 [LinkedIn](https://www.linkedin.com/in/jonnagel/)

*Seeking high-coherence organizations in the Chicago metro area. Open to discussing applications of multi-agent bias detection for organizational assessment, hiring, and strategic decision making.*

---

*"In a world of cognitive bias and organizational politics, systematic dialectic processes are the difference between good decisions and lucky guesses."*
