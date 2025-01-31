import csv
import requests

# Replace with your GitHub info
GITHUB_TOKEN = "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"
REPO_OWNER = "hit3p48cy"
REPO_NAME = "GitHubRepo"

def create_issue(title, body, labels):
    url = f"https://api.github.com/repos/hit3p48cy/GitHubRepo/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"title": title, "body": body, "labels": labels.split(",")}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Read issues from CSV and create them in GitHub
with open("issue_csv_project.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        result = create_issue("T3", row["body"], row["labels"])
        
        print(f"Issue created: {result.get('html_url', 'Error')}")

print("All issues imported!")
