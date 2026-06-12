from sqlalchemy.orm import Session

from app.integrations.github.fetcher import GitHubFetcher
from app.models.github_update import GitHubUpdate


class GitHubSyncService:
    def __init__(self, db: Session):
        self.db = db
        self.fetcher = GitHubFetcher()

    def sync_subscription(self, subscription):
        commits = self.fetcher.fetch_commits(subscription.owner, subscription.repo)

        results = []

        for item in commits:
            update = GitHubUpdate(
                repo_full_name=f"{subscription.owner}/{subscription.repo}",
                update_type="commit",
                title=item["commit"]["message"].split("\n")[0],
                url=item["html_url"],
                author=item["commit"]["author"]["name"],
            )
            self.db.add(update)
            results.append(update)

        self.db.commit()

        return results
