from sqlalchemy.orm import Session

from app.services.subscription_service import SubscriptionService
from app.services.github_sync_service import GitHubSyncService
from app.services.report_service import ReportService
from app.notifications.manager import NotificationManager


class SentinelService:
    def __init__(self, db: Session):
        self.db = db
        self.subscription_service = SubscriptionService(db)
        self.sync_service = GitHubSyncService(db)
        self.report_service = ReportService(db)
        self.notification_manager = NotificationManager()

    def run_once(self):
        subscriptions = self.subscription_service.list_enabled()
        reports = []

        for sub in subscriptions:
            updates = self.sync_service.sync_subscription(sub)
            repo_full_name = f"{sub.owner}/{sub.repo}"
            report = self.report_service.create_report(
                repo_full_name=repo_full_name,
                updates=[u.title for u in updates],
                period=sub.frequency,
            )
            self.notification_manager.send_all(report.content)
            reports.append(report)

        return reports
