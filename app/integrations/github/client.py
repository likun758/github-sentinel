import httpx
from app.core.config import settings


class GitHubClient:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {settings.github_token}",
            "Accept": "application/vnd.github+json",
        }

    def get(self, path: str, params: dict | None = None):
        url = f"{self.base_url}{path}"
        response = httpx.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
