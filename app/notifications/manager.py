from app.notifications.webhook import WebhookNotifier


class NotificationManager:
    def __init__(self):
        self.notifiers = [
            WebhookNotifier(),
        ]

    def send_all(self, content: str):
        for notifier in self.notifiers:
            notifier.send(content)
