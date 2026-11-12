# 🔍 Trace a LangChain App with LangSmith

## 📌 Project Overview

This project demonstrates how to build a simple LangChain application using OpenAI and monitor its execution through LangSmith.

The application sends three different prompts to an OpenAI language model using LangChain's `ChatOpenAI` integration. LangSmith automatically records the execution traces without requiring any manual tracing code in the application.

The project helps understand how to monitor:

- Actual prompts sent to the AI model.
- AI-generated responses.
- Execution latency.
- Input and output token usage.
- Token consumption and API cost.

## 🎯 Objectives

1. Build a basic LangChain application using Python.
2. Connect LangChain with OpenAI using `ChatOpenAI`.
3. Configure LangSmith tracing through environment variables.
4. Execute three different prompts in a single application run.
5. Monitor application execution using the LangSmith dashboard.
6. Compare token usage, latency and estimated API costs.

## 🏗️ System Architecture

```text
Python Application
     |
     v
traced_app.py
     |
     v
LangChain (ChatOpenAI)
     |
     v
OpenAI API
     |
     +------> AI Generated Responses
     |
     v
LangSmith Automatic Tracing
     |
     v
LangSmith Dashboard
     |
     +------> Input Prompts
     +------> Output Responses
     +------> Latency
     +------> Token Usage
     +------> Run Details
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | LLM application framework |
| ChatOpenAI | OpenAI model integration |
| OpenAI API | AI response generation |
| LangSmith | Execution tracing and monitoring |
| python-dotenv | Environment variable management |
| VS Code | Development environment |

## 📁 Project Structure

```text
LangChain_Tracing_Assignment/
│
├── venv/
│
├── .env
│
├── .gitignore
│
├── traced_app.py
│
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows CMD:

```cmd
venv\Scripts\activate
```

### Step 2: Install required packages

```bash
pip install langchain langchain-openai langsmith python-dotenv
```

### Step 3: Configure API keys

Create a `.env` file in the project folder.

Add the following environment variables:

```env
OPENAI_API_KEY=your_openai_api_key

LANGSMITH_API_KEY=your_langsmith_api_key

LANGSMITH_TRACING=true

LANGSMITH_PROJECT=Rajesh_LangChain_Tracing
```

**Security Note:** Never upload your `.env` file or expose your API keys publicly.

### Step 4: Load environment variables

At the beginning of `traced_app.py`, add:

```python
from dotenv import load_dotenv

load_dotenv()
```

This loads the environment variables before the LangChain model is initialized.

## 🧪 Application Details

### AI Model

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

### Three Prompts

**Prompt 1 – Basic**

Topic: Internet of Things (IoT).

Objective: Generate a short explanation of IoT.

**Prompt 2 – Technical**

Topic: Industrial Temperature Sensor Integration.

Objective: Explain communication between sensors, PLC and SCADA systems.

**Prompt 3 – Detailed**

Topic: IoT-Based Marine Weather Monitoring System.

Objective: Develop a detailed technical implementation plan covering:

- Weather sensors.
- Data acquisition system.
- RS485 and Modbus communication.
- Edge computer and data logger.
- GSM/4G communication.
- Cloud server and database.
- Real-time web dashboard.

### Application Execution

Run the application:

```cmd
python traced_app.py
```

The application executes all three prompts sequentially and prints their AI-generated responses in the terminal.

## 📊 LangSmith Tracing and Monitoring

LangSmith automatically captures execution details when tracing is enabled through environment variables.

**LangSmith Dashboard:** https://smith.langchain.com/

**Project Name:** `Rajesh_LangChain_Tracing`

The following information can be inspected for each run:

| Parameter | Description |
|---|---|
| Input | Exact prompt sent to the model |
| Output | AI-generated response |
| Latency | Time taken to execute the request |
| Input Tokens | Tokens used in the input prompt |
| Output Tokens | Tokens generated in the response |
| Total Tokens | Combined input and output tokens |

## 💰 Token Usage and Cost Analysis

The three prompts have different levels of complexity.

| Prompt | Complexity | Expected Token Usage |
|---|---|---|
| Prompt 1 | Basic | Low |
| Prompt 2 | Technical | Medium |
| Prompt 3 | Detailed | High |

*These are expected trends, not measured results. Actual usage must be collected from LangSmith.*

### Cost Calculation

```text
Total Cost =
(Input Tokens × Input Token Rate)
+
(Output Tokens × Output Token Rate)
```

The actual cost depends on the selected model's API pricing.

### Key Learning

A detailed prompt may consume more tokens, but higher token consumption should provide meaningful additional value.

The objective is to evaluate whether the additional response quality and technical detail justify the increased API cost.

## 🔐 Security and GitHub Configuration

Create a `.gitignore` file:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

This prevents API credentials and local virtual environment files from being included in Git commits.

## 📚 Key Learnings

Through this assignment, I learned:

1. How to integrate OpenAI with LangChain using `ChatOpenAI`.
2. How to configure API keys using environment variables.
3. How to enable LangSmith tracing without adding tracing functions to the application.
4. How to monitor AI application execution.
5. How to inspect prompts, responses, latency and token consumption.
6. How to compare prompt complexity and API usage.
7. Why observability is important when developing reliable AI applications.

## 🚀 Future Improvements

- Build a Streamlit-based AI monitoring dashboard.
- Compare different OpenAI models.
- Evaluate response quality and token efficiency.
- Develop an AI-powered sensor monitoring assistant.
- Integrate real-time IoT sensor data with LangChain.

## 👨‍💻 Author

**Rajesh B**

Project Engineer | Electrical, Electronics & Instrumentation

Technical Interests:
- Industrial Instrumentation
- Sensor Integration and Data Acquisition
- IoT and Cloud Communication
- Python and Generative AI
- AI Application Development

---

*This project is part of my continuous learning journey in Python, LangChain and Generative AI.*