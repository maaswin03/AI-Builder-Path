# 🕷️ Web Crawler Agent using AWS Bedrock

## Overview

This project implements a Web Crawler Agent using AWS Bedrock Agents and AWS Lambda. The agent accepts a webpage URL from the user, invokes a custom Lambda tool to scrape and clean the webpage, and returns a summarized response through a Streamlit frontend.

---

## Architecture

User
↓
Streamlit Frontend
↓
AWS Bedrock Agent
↓
Action Group (web_scrape Tool)
↓
AWS Lambda
↓
Requests + BeautifulSoup
↓
Webpage Content
↓
Bedrock Agent Response
↓
Frontend

---

## Features

- Crawl webpages from user-provided URLs
- Automatic tool invocation using AWS Bedrock Agents
- HTML cleaning using BeautifulSoup
- Handles redirects and gzip-compressed responses
- Streamlit web interface
- AWS Lambda serverless execution

---

## Tech Stack

- AWS Bedrock Agents
- AWS Lambda
- Python
- Requests
- BeautifulSoup4
- Streamlit
- Boto3

---

## Project Structure

task-2/
├── frontend/
│   └── app.py
├── lambda/
│   └── lambda_function.py
├── test_agent.py
├── requirements.txt
└── README.md

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd task-2
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure AWS

Configure AWS credentials:

```bash
aws configure
```

Create a `.env` file:

```text
AWS_REGION=eu-north-1
BEDROCK_AGENT_ID=<your-agent-id>
BEDROCK_AGENT_ALIAS_ID=<your-agent-alias-id>
```

---

## Run

```bash
streamlit run frontend/app.py
```

---

## Example

Input:

```
Crawl this URL: https://example.com
```

Output:

```
The webpage at https://example.com contains information about Example Domain...
```

---

## Screenshots

- Streamlit Frontend
- AWS Lambda Function
- AWS Bedrock Agent

---

## Author

Aswin