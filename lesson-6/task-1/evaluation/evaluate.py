import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import time

from agent.graph import graph

with open("evaluation/test_cases.json") as f:
    tests = json.load(f)

results = []

for test in tests:

    start = time.time()

    response = graph.invoke(
        {
            "query": test["query"]
        }
    )

    latency = round(time.time() - start, 2)

    results.append(
        {
            "query": test["query"],
            "latency": latency,
            "answer": response["answer"]
        }
    )

print(json.dumps(results, indent=2))