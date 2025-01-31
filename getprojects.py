from github import Github
import requests


# Replace with your GitHub Personal Access Token
GITHUB_TOKEN = "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"

# Replace with your repository details
REPO_OWNER = "hit3p48cy"  # This could be a user or organization
REPO_NAME = "GitHubRepo"

# Replace with your project details
PROJECT_NAME = "TaskManagementNew"
PROJECT_BODY = "This is a test project created via API."

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/projects"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.inertia-preview+json"
}

data = {
    "name": PROJECT_NAME,
    "body": PROJECT_BODY
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Project created successfully:", response.json()["html_url"])
else:
    print("Failed to create project:", response.json())
