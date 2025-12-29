# 🧠 Ahoum Conversation Evaluation Benchmark

A production-ready benchmark system for evaluating conversational AI models across multiple dimensions including linguistic quality, pragmatics, safety, emotion, and behavioral traits.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Goals & Requirements](#-goals--requirements)
- [System Architecture](#-system-architecture)
- [Benchmark Dataset](#-benchmark-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technical Challenges & Solutions](#-technical-challenges--solutions)
- [Project Structure](#-project-structure)
- [Deliverables](#-deliverables)

---

## 📌 Project Overview

This project implements a **production-ready benchmark system** for evaluating conversational AI models across **300+ distinct facets** covering:

- **Linguistic Quality** — Grammar, coherence, and language proficiency
- **Pragmatics** — Contextual understanding and appropriateness
- **Safety** — Content moderation and harmful content detection
- **Emotion** — Emotional awareness and response quality
- **Behavioral & Psychological Traits** — Personality indicators and psychological patterns

Each conversation turn is scored on a **five-level ordered scale** with an associated **confidence score**. The architecture is designed to **scale beyond 5000 facets without any redesign**, ensuring future extensibility and maintainability.

---

## ✨ Features

- ✅ Multi-faceted evaluation system (300+ facets, extensible to 5000+)
- ✅ Five-level ordered scoring with confidence metrics
- ✅ Fault-tolerant execution with checkpoint recovery
- ✅ Support for open-weights models (≤16B parameters)
- ✅ Dockerized deployment for consistent environments
- ✅ Interactive Streamlit UI for result visualization
- ✅ Robust JSON validation and error handling
- ✅ Dynamic batching for efficient processing

---

## 🎯 Goals & Requirements

| Requirement | Status |
|------------|--------|
| Evaluate every conversation turn | ✅ |
| 300+ facets | ✅ |
| Five-level ordered scoring | ✅ |
| Confidence per score | ✅ |
| Supports ≥ 5000 facets | ✅ |
| Open-weights model ≤16B | ✅ (Qwen / Llama-class models) |
| No one-shot prompt | ✅ |
| Fault-tolerant execution | ✅ |
| Dockerized baseline | ✅ |
| Sample UI (Streamlit) | ✅ |

---

## 🧱 System Architecture

```
Facets CSV
    ↓
Loader → Preprocessor → Facet Engine
    ↓
Batch Controller
    ↓
LLM Scorer (Open-weight model)
    ↓
JSON Validator & Extractor
    ↓
Checkpoint Engine
    ↓
CSV / JSON Results
```

### Core Components

- **Loader Module** — Efficiently loads and parses facet dataset
- **Preprocessor** — Cleans and enriches facet metadata
- **Facet Engine** — Dynamically manages and batches facets for scalable processing
- **Scorer** — Executes evaluation with confidence scoring using open-weights models
- **Main Pipeline** — Orchestrates the complete benchmark workflow
- **Checkpoint System** — Crash-safe recovery mechanism for long-running evaluations
- **UI Dashboard** — Streamlit-based visualization and analysis interface

---

## 🧪 Benchmark Dataset

The benchmark includes **50+ conversations** covering diverse scenarios:

- Emotional distress and support
- Hostility and safety-critical cases
- Happiness and optimistic interactions
- Technical problem-solving scenarios
- Professional conflict resolution
- Mental health indicators

Each conversation is evaluated against **all configured facets**, providing comprehensive multi-dimensional analysis.

---

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Docker (optional, for containerized deployment)
- GPU recommended (optional, for faster inference)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ahoum-read-me
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python main.py --help
   ```

---

## 🚀 Usage

### Local Execution

Run the benchmark pipeline:

```bash
python main.py
```

Results will be saved as:
- `benchmark_results.csv`
- `benchmark_results.json`

### Docker Deployment

**Build the image:**
```bash
docker build -t ahoum-benchmark .
```

**Run the container:**
```bash
docker run -p 8501:8501 ahoum-benchmark
```

### Streamlit UI

Launch the interactive dashboard:

```bash
streamlit run ui/app.py
```

Access the UI at `http://localhost:8501`

---

## 🧗 Technical Challenges & Solutions

### Challenge 1: Extremely Long Execution Time

**Problem:**  
Evaluating hundreds of facets across dozens of conversations caused frequent disconnections and total progress loss in cloud environments.

**Solution:**  
Implemented a **checkpoint-based execution engine** that saves progress after every conversation. The pipeline automatically resumes from the last completed conversation in case of interruptions, ensuring no work is lost.

---

### Challenge 2: Inconsistent JSON Output from the Model

**Problem:**  
Language models sometimes returned malformed, partial, or non-standard JSON responses, causing pipeline failures.

**Solution:**  
Built a **robust extraction and validation layer** that:
- Isolates valid JSON from model responses
- Enforces schema correctness
- Safely skips corrupted rows with error logging
- Provides fallback mechanisms for edge cases

---

### Challenge 3: Scaling Beyond 300 Facets

**Problem:**  
Hard-coded logic and static configurations fail at large scale, making it difficult to extend beyond initial requirements.

**Solution:**  
The **Facet Engine** dynamically loads and batches facets from configuration files. The architecture supports **5000+ facets without any redesign**, using scalable data structures and processing pipelines.

---

### Challenge 4: Preventing One-Shot Prompting

**Problem:**  
One-shot prompting approaches fail at scale and violate assignment constraints for large facet evaluations.

**Solution:**  
Facets are evaluated in **controlled batches** with optimized prompt engineering, ensuring stability, compliance, and consistent performance across all evaluation dimensions.

---

### Challenge 5: Hardware Limitations

**Problem:**  
Limited memory and runtime constraints in cloud notebook environments made it difficult to complete full benchmark runs.

**Solution:**  
Dynamic batching combined with checkpoint recovery enables reliable execution across diverse hardware configurations (CPU, GPU, cloud instances). The system adapts batch sizes based on available resources.

---

## 📁 Project Structure

```
.
├── loader.py              # Facet dataset loader
├── preprocessor.py        # Metadata preprocessing
├── facet_engine.py        # Dynamic facet management
├── scorer.py              # LLM-based evaluation scorer
├── main.py                # Main pipeline orchestrator
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
├── checkpoints/           # Checkpoint storage
├── ui/                    # Streamlit dashboard
│   └── app.py
└── README.md              # Project documentation
```

---

## 📦 Deliverables

- ✅ Full source code with comprehensive documentation
- ✅ Dockerized pipeline for reproducible deployments
- ✅ Streamlit UI for interactive result analysis
- ✅ 50+ conversation benchmark dataset
- ✅ CSV and JSON evaluation results
- ✅ Fault-tolerant benchmark engine with checkpoint recovery
- ✅ Scalable architecture supporting 5000+ facets

---

## 🧾 Conclusion

This benchmark framework provides a **scalable, reliable, and production-ready solution** for deep conversational evaluation across linguistic, emotional, and safety dimensions. The system meets and exceeds all assignment requirements while providing a foundation for future research and development in conversational AI evaluation.

---

## 📄 License

[Specify your license here]

## 🤝 Contributing

[Contributing guidelines, if applicable]

## 📧 Contact

[Contact information or issue tracker]
