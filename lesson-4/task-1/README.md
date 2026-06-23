# Internal Research Agent using LangChain & LangGraph

## Overview

This project implements an **Internal Research Agent** that helps answer organizational queries by intelligently selecting the appropriate information source.

The agent is built using **LangGraph**, **LangChain**, **Google Gemini**, **FAISS**, and **Google Docs API**. It routes user queries to the most suitable tool and returns concise, AI-generated responses.

---

## Features

* HR Policy Retrieval using RAG
* Google Docs Integration
* Web Search for Industry Trends
* LangGraph-based Tool Routing
* AI-generated Responses using Gemini
* Modular and Extensible Architecture

---

## Architecture

```text
                    User Query
                         │
                         ▼
             Internal Research Agent
                   (LangGraph)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   RAG Tool        Google Docs Tool   Web Search Tool
   (HR Policy)      (Insurance)      (Industry Data)
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                    Google Gemini
                         │
                         ▼
                  Final AI Response
```

---

## Project Structure

```text
task-1/
│
├── agent/
│   ├── graph.py
│   └── nodes.py
│
├── documents/
│   └── hr_policy.txt
│
├── mcp/
│   └── google_docs.py
│
├── rag/
│   ├── retriever.py
│   └── vector_store.py
│
├── tools/
│   ├── rag_tool.py
│   ├── web_search_tool.py
│   └── mcp_tool.py
│
├── vector_db/
│   ├── hr_index.faiss
│   └── hr_chunks.pkl
│
├── .env
├── credentials.json
├── requirements.txt
├── main.py
└── README.md
```

---

## Technologies Used

* Python
* LangChain
* LangGraph
* Google Gemini
* FAISS
* Sentence Transformers
* Google Docs API
* DDGS (DuckDuckGo Search)

---

## Tools

### 1. RAG Tool

Retrieves information from HR policy documents stored in a FAISS vector database.

Example:

* Leave Policy
* Working Hours
* Work From Home Policy
* AI Data Handling Policy

---

### 2. Google Docs Tool

Reads insurance-related documents from Google Docs using the Google Docs API.

Example:

* Refund Policy
* Claims
* Coverage
* Customer Support

---

### 3. Web Search Tool

Fetches current information from the web, including:

* Industry Benchmarks
* AI Regulations
* Technology Trends
* Compliance Updates

---

## Sample Queries

### HR Policy

```text
How many casual leaves are employees entitled to?
```

### Insurance

```text
Summarize the insurance policy.
```

### Web Search

```text
Latest AI regulations.
```

### Industry Research

```text
Compare AI regulations with company policy.
```

---

## Workflow

1. User submits a query.
2. LangGraph routes the query to the appropriate tool.
3. The selected tool retrieves relevant information.
4. Google Gemini generates a concise response.
5. The final answer is returned to the user.

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd task-1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Add your Google OAuth credentials:

```text
credentials.json
```

to the project root.

---

## Run the Project

```bash
python3 main.py
```

---

## Example Output

### Input

```text
How many casual leaves are employees entitled to?
```

### Output

```text
Employees are entitled to 12 casual leaves and 12 sick leaves annually.
```

---

## Future Enhancements

* LLM-based Supervisor Agent
* Multi-Agent Collaboration
* Multiple RAG Knowledge Bases
* PDF & SharePoint Integration
* Conversation Memory
* Role-Based Access Control

---

## Conclusion

This project demonstrates how LangGraph, LangChain, Retrieval-Augmented Generation (RAG), Google Docs, and Web Search can be integrated into a single Internal Research Agent capable of delivering accurate, contextual, and AI-generated responses for organizational knowledge retrieval.
