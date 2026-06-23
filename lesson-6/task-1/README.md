# Multi-Agent Support System using LangGraph

## Overview

This project implements a **Multi-Agent Support System** using **LangGraph**, **LangChain**, and **Google Gemini**.

The system contains a **Supervisor Agent** that classifies user queries into either **IT** or **Finance** and routes them to the appropriate specialist agent. Each specialist agent combines information from internal documents and web search results to generate accurate, AI-powered responses.

---

# Features

* Supervisor Agent for intelligent query routing
* IT Support Agent
* Finance Support Agent
* Internal document retrieval
* Web search integration
* AI-powered responses using Google Gemini
* LangGraph workflow orchestration

---

# Architecture

```text
                    User Query
                         │
                         ▼
                 Supervisor Agent
              (Classifies the Query)
                  /             \
                 /               \
                ▼                 ▼
          IT Support Agent   Finance Agent
                │                 │
         ReadFile Tool      ReadFile Tool
                │                 │
         Web Search Tool    Web Search Tool
                │                 │
                └────────┬────────┘
                         ▼
                    Google Gemini
                         │
                         ▼
                  Final AI Response
```

---

# Project Structure

```text
task-1/
│
├── agent/
│   ├── graph.py
│   ├── supervisor.py
│   ├── it_agent.py
│   └── finance_agent.py
│
├── documents/
│   ├── it_policy.txt
│   └── finance_policy.txt
│
├── tools/
│   ├── read_file_tool.py
│   └── web_search_tool.py
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* LangGraph
* LangChain
* Google Gemini
* DDGS (DuckDuckGo Search)
* Python Dotenv

---

# Agents

## Supervisor Agent

Responsible for classifying user queries into one of two categories:

* IT
* Finance

The query is then routed to the appropriate specialist agent.

---

## IT Agent

Handles all IT-related requests.

### Internal Knowledge

* VPN Setup
* Approved Software
* Laptop Requests
* Password Reset
* Email Configuration
* Antivirus Policy

### External Knowledge

Uses web search to provide additional technical guidance.

---

## Finance Agent

Handles all finance-related requests.

### Internal Knowledge

* Payroll
* Expense Reimbursement
* Budget Reports
* Travel Claims
* Purchase Orders
* Invoice Processing

### External Knowledge

Uses web search to supplement finance-related information.

---

# Workflow

1. User submits a query.
2. Supervisor Agent classifies the query.
3. LangGraph routes the request.
4. IT Agent or Finance Agent processes the query.
5. Internal documents are read.
6. Web search retrieves additional information.
7. Google Gemini generates the final response.
8. Response is returned to the user.

---

# Example Queries

### IT

```
How do I set up VPN?
```

```
How do I request a new laptop?
```

```
What software is approved for use?
```

---

### Finance

```
When is payroll processed?
```

```
How do I file a reimbursement?
```

```
Where can I find monthly budget reports?
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd task-1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run

```bash
python3 main.py
```

---

# Sample Output

### Input

```
How do I set up VPN?
```

### Output

```
Employees should install Cisco AnyConnect VPN from the company portal.

Additionally, configure the VPN using your corporate credentials and ensure the connection is active before accessing internal resources.
```

---

# Future Enhancements

* Add HR Support Agent
* Add Database Integration
* Add Conversation Memory
* Add Role-Based Authentication
* Integrate Company Knowledge Base
* Add Support Ticket Creation

---

# Conclusion

This project demonstrates a LangGraph-based multi-agent architecture where a Supervisor Agent intelligently routes user queries to specialized IT and Finance agents. By combining internal documentation, web search, and Google Gemini, the system delivers contextual and accurate responses suitable for enterprise support scenarios.
