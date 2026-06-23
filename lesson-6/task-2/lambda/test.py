from lambda_function import lambda_handler

event = {
    "url": "https://example.com"
}

print(lambda_handler(event, None))