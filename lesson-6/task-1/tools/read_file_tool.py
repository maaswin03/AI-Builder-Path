import os


def read_file(category):
    """
    Read IT or Finance policy file.
    """

    if category == "it":
        file_path = "documents/it_policy.txt"

    elif category == "finance":
        file_path = "documents/finance_policy.txt"

    else:
        return "No document found."

    if not os.path.exists(file_path):
        return "Document not found."

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()