from app.notifications.base import BaseNotifier


class WebhookNotifier(BaseNotifier):
    def send(self, content: str):
        print(content)
