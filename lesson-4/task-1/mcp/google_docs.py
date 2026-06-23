from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]

def get_google_doc(document_id):
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    service = build("docs", "v1", credentials=creds)

    document = service.documents().get(documentId=document_id).execute()

    content = ""

    for element in document.get("body").get("content"):
        if "paragraph" in element:
            for text_run in element["paragraph"].get("elements", []):
                if "textRun" in text_run:
                    content += text_run["textRun"]["content"]

    return content