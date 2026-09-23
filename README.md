# 🏦 Insurance Claims Agentic AI

AI-assisted insurance claims decision-support platform built using a multi-agent architecture.

## 📌 Overview

This project demonstrates how multiple AI agents can work together to analyze insurance claim information, retrieve relevant policy knowledge, review potential fraud indicators, and generate a structured assessment report.

The system is designed as an educational decision-support prototype with human review in the final decision process.
## 🏗️ System Architecture

👤 Claim Submission
        ↓
🎯 Orchestrator Agent
        ↓
📄 Document Agent
📋 Policy Agent
🔎 Assessment Agent
🚨 Fraud Indicator Agent
        ↓
📝 Report Agent
        ↓
👨‍💼 Human Review

## 🤖 Agents

### 🎯 Orchestrator Agent
Coordinates the complete claims analysis workflow.

### 📄 Document Agent
Reviews submitted claim information and identifies required supporting documents.

### 📋 Policy Agent
Retrieves relevant policy information using TF-IDF and cosine similarity.

### 🔎 Assessment Agent
Reviews claim information against retrieved policy knowledge.

### 🚨 Fraud Indicator Agent
Identifies potential indicators that may require further investigation.

### 📝 Report Agent
Combines agent outputs into a structured claims assessment report.
## ✨ Features

- Multi-agent claims analysis
- Policy knowledge retrieval
- TF-IDF based document retrieval
- Cosine similarity
- Fraud indicator review
- Structured assessment report
- Human-in-the-loop review
- Streamlit web interface
- Safety and decision-support controls

## 🛠️ Technology Stack

- Python
- Scikit-learn
- Streamlit
- TF-IDF
- Cosine Similarity
- Multi-Agent Architecture
- GitHub Codespaces

## 🌐 Web Interface

The project includes a Streamlit dashboard where users can:

1. Enter insurance claim details
2. Start multi-agent analysis
3. View document findings
4. View retrieved policy information
5. Review assessment results
6. Review fraud indicators
7. View human review requirements
## 🧪 Example Claim

```text
Car accident claim - vehicle damaged in a collision.
Repair estimate is 85000 INR.
```
The system produces a structured report containing:

- Document Review
- Policy Review
- Claim Assessment
- Fraud Indicator Review
- Human Review

## 📁 Project Structure
```text
insurance-claims-agentic-ai/
│
├── agents/
│   ├── orchestrator.py
│   ├── document_agent.py
│   ├── policy_agent.py
│   ├── assessment_agent.py
│   ├── fraud_agent.py
│   └── report_agent.py
│
├── knowledge/
│   └── policy_notes.txt
│
├── app.py
├── main.py
├── .gitignore
└── README.md
## ▶️ Run Locally

Install dependencies:

bash
pip install scikit-learn streamlit
python main.py
streamlit run app.py
## ⚠️ Safety and Limitations

This project is an educational insurance claims decision-support prototype.

It does **not** automatically approve or reject insurance claims and does **not** establish fraud.

Fraud indicators require further investigation.

Final claim decisions should be made by authorized insurance professionals based on applicable policy terms, evidence, regulations, and organizational procedures.

Only synthetic or demonstration data should be used with this project. Do not use real customer or personally identifiable insurance information.

## 👨‍💻 Author

**Sathia23456**

GitHub:  
https://github.com/Sathia23456
