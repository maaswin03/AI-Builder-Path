import json
import gzip
import requests
from bs4 import BeautifulSoup


MAX_SIZE = 2 * 1024 * 1024  # 2 MB


def scrape_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15,
        allow_redirects=True,
        stream=True,
    )

    content = response.raw.read(MAX_SIZE)

    if response.headers.get("Content-Encoding") == "gzip":
        content = gzip.decompress(content)

    html = content.decode("utf-8", errors="ignore")

    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return text[:5000]


def lambda_handler(event, context):

    url = event.get("url")

    if not url:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {
                    "error": "URL is required"
                }
            ),
        }

    try:
        result = scrape_url(url)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "url": url,
                    "content": result,
                }
            ),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "error": str(e)
                }
            ),
        }