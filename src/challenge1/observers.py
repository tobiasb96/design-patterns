from typing import Any

from .issue import Issue, IssueObserver


class EmailNotifier(IssueObserver):
    def __init__(self, email_address: str) -> None:
        self.email_address = email_address

    def update(self, issue: Issue, changed_fields: dict[str, Any]) -> None:
        # In a real implementation, this would send an actual email
        for _field, _changes in changed_fields.items():
            pass


class SlackNotifier(IssueObserver):
    def __init__(self, channel: str) -> None:
        self.channel = channel

    def update(self, issue: Issue, changed_fields: dict[str, Any]) -> None:
        # In a real implementation, this would send a Slack message
        for _field, _changes in changed_fields.items():
            pass


class LoggingObserver(IssueObserver):
    def update(self, issue: Issue, changed_fields: dict[str, Any]) -> None:
        # In a real implementation, this would write to a log file
        for _field, _changes in changed_fields.items():
            pass
