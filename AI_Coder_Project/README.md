# Auto-Coding Multi-Agent System: arXiv CS Daily Generator

## 📖 Project Overview
This project implements a **Multi-Agent System** driven by LLM (DeepSeek) to autonomously generate fully functional web applications. 

The system demonstrates "Agentic Workflow" by orchestrating specialized agents (Planner, Coder) to build an **arXiv CS Daily** website from scratch, featuring domain-specific navigation, PDF viewing, and BibTeX citation tools.

## 🏗️ Architecture
The system consists of three core components:
1.  **Planner Agent**: Analyzes high-level requirements and decomposes them into a precise file generation plan.
2.  **Coder Agent**: specialized in Web Development (HTML/CSS/JS), capable of strictly following UI/UX constraints.
3.  **Orchestrator (Main)**: Manages the workflow loop and context passing between agents.

## 🚀 Setup & Execution

### Prerequisites
*   Python 3.8+
*   DeepSeek API Key (compatible with OpenAI SDK)

### Installation
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1.  Open `src/coder.py` and `src/planner.py`, and input your API Key.
2.  Run the main orchestration script:
    ```bash
    python src/main.py
    ```
3.  The system will automatically generate the website in the `workspace/` directory.
4.  Open `workspace/index.html` in your browser to view the result.

## 💻 Key Features
*   **Automated Full-Stack Generation**: Generates HTML, CSS, and JS simultaneously.
*   **Strict UI Enforcement**: Implements high-contrast styling and responsive layout via specific prompting.
*   **Interactive Logic**: Implements complex JS logic (Clipboard API, DOM manipulation) for real-world usability.