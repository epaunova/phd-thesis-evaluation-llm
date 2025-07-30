# 🧠 Reliable Evaluation & Drift Detection in Large Language Models (LLMs)
https://doi.org/10.5281/zenodo.16615347

> A research-grade project showcasing methods for hallucination detection, prompt drift scoring, and GPU-efficient inference for production-grade LLMs.

![drift](./figures/drift_comparison_chart.png)

## 📌 Overview

This project simulates a real-world ML/AI research workflow for **reliable LLM evaluation** across model versions and prompt variations. It includes:

- Hallucination detection and factuality scoring  
- Prompt drift detection using tone, length, and instruction adherence metrics  
- Latency and cost benchmarking across GPT-4, Claude 3, and Mixtral  
- Streamlit dashboards for visual comparison and exploratory evaluation  
- Simulated experimental dataset with realistic LLM outputs and scoring  

🧪 Designed to serve as a **proof-of-concept** for AI safety, GenAI product evaluation, and R&D workflows in enterprise settings.

---

## 📁 Project Structure

PhD_Thesis_Repo/
├── data/ # Simulated LLM outputs and scoring metadata
│ ├── hallucination_gpt4.csv
│ └── drift_samples_claude.csv
├── figures/ # Diagrams for latency, hallucination, drift metrics
│ ├── hallucination_histogram.png
│ └── drift_comparison_chart.png
├── src/ # Core Python logic
│ ├── hallucination_detector.py
│ └── drift_scoring.py
├── notebooks/ # Jupyter notebooks for data exploration
│ ├── 01_data_eda.ipynb
│ └── 02_llm_eval_comparison.ipynb
├── README.md
└── requirements.txt

yaml
Copy
Edit

---

## 🔬 Features

- ✅ **Hallucination Detection** using keyword-based scoring and GPT-graded evaluation  
- ✅ **Prompt Drift Detection** with rubric-based scoring on tone, length, verbosity  
- ✅ **Streamlit UI** for visual exploration of model behavior  
- ✅ **Metrics Dashboard** for latency, output quality, hallucination rate  
- ✅ **Energy/Inference Tradeoff** insights via simulated benchmarks  
- ✅ Designed for **enterprise LLM evaluation pipelines**  

---

## 📊 Example Outputs

| Model     | Hallucination Rate | Latency (ms) | Prompt Drift Score |
|-----------|--------------------|--------------|---------------------|
| GPT-4     | 8.5%               | 1025         | 0.32                |
| Claude 3  | 7.2%               | 875          | 0.41                |
| Mixtral   | 12.1%              | 495          | 0.62                |

---

## 🛠 Tech Stack

- Python · pandas · scikit-learn  
- Streamlit · matplotlib · seaborn  
- Simulated data with GPT-4/Claude-style outputs  
- Jupyter/Colab Notebooks for EDA  
- GitHub Actions ready for CI  

---

## ✍️ Author

**Eva Paunova**  
PhD Researcher (in progress) in AI Evaluation  
GitHub: [@epaunova](https://github.com/epaunova)  
Medium: [@evapaunova](https://medium.com/@evapaunova)  

---
