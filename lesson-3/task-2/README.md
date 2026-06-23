# Smart Gmail Agent using n8n

## Overview

This project implements a Smart Gmail Agent using n8n. The workflow classifies incoming support queries as either **Customer** or **Admin**, retrieves users from the provided API, filters users based on their role, and sends an email to the appropriate recipient.

## Workflow

1. Receive a support query.
2. Classify the query using AI.
3. Fetch users from the provided API.
4. Filter users based on their role (Customer/Admin).
5. Send an email to the matching user(s).

## Technologies Used

* n8n
* Google Gemini
* HTTP Request Node
* Gmail Node

## Repository Structure

```text
workflow/
screenshots/
demo/
README.md
```

## Test Scenarios

### Customer Query

* Classified as **Customer**
* Email routed to customer users

### Admin Query

* Classified as **Admin**
* Email routed to admin users

## Conclusion

This workflow demonstrates AI-based query classification, API integration, conditional routing, and automated email delivery using n8n.
