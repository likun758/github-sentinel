from datetime import datetime, timedelta
from app.integrations.github.client import GitHubClient


class GitHubFetcher:
    def __init__(self):
        self.client = GitHubClient()

    def fetch_commits(self, owner: str, repo: str, days: int = 1):
        since = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"

        return self.client.get(
            f"/repos/{owner}/{repo}/commits",
            params={"since": since},
        )

    def fetch_releases(self, owner: str, repo: str):
        return self.client.get(f"/repos/{owner}/{repo}/releases")

    def fetch_pull_requests(self, owner: str, repo: str):
        return self.client.get(
            f"/repos/{owner}/{repo}/pulls",
            params={"state": "all"},
        )

    def fetch_issues(self, owner: str, repo: str):
        return self.client.get(
            f"/repos/{owner}/{repo}/issues",
            params={"state": "all"},
        )
