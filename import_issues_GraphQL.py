from github import Github
import requests

# Authenticate with GitHub
g = Github("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")

# Get the repository
repo = g.get_repo("hit3p48cy/GitHubRepo")

# Create an issue
issue = repo.create_issue(title="New Issue1", body="This is the body of the issue.")
print(f"Issue created: {issue.html_url}")

# Get the issue node ID
issue_node_id = issue.raw_data['node_id']

# GitHub GraphQL API endpoint
url = 'https://api.github.com/graphql'

# Your GitHub token
headers = {
    'Authorization': 'Bearer your_github_token',
    'Content-Type': 'application/json',
}

# GraphQL query to add an issue to a project


query = """
mutation ($projectId: ID!, $issueNodeId: ID!) {
  addProjectV2ItemById(input: {projectId: $projectId, contentId: $issueNodeId}) {
    item {
      id
    }
  }
}
"""
query = """
mutation{
  addProjectV2ItemById(input: {projectId: "PVT_kwHOC0XxgM4AxNSu", contentId: "I_kwDONyVKdM6oToLO"}) {
    item {
      id
    }
  }
}
"""
# Replace with your project ID and issue node ID
variables = {
    "projectId": "PVT_kwHOC0XxgM4AxNSu",  # Replace with your project ID
    "issueNodeId": issue_node_id,  # Use the issue node ID
}

# Make the request
response = requests.post(url, json={'query': query}, headers=headers)

# Check the response
if response.status_code == 200:
    print("Issue assigned to project successfully!")
else:
    print("Failed to assign issue to project.")
    print(response.json())
