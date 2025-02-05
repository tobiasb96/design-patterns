from typing import Dict, Any
from .issue import IssueObserver, Issue


class EmailNotifier(IssueObserver):
    def __init__(self, email_address: str):
        self.email_address = email_address

    def update(self, issue: Issue, changed_fields: Dict[str, Any]) -> None:
        # In a real implementation, this would send an actual email
        print(f"Sending email to {self.email_address}:")
        print(f"Issue '{issue.title}' has been updated:")
        for field, changes in changed_fields.items():
            print(f"- {field}: {changes['old']} → {changes['new']}")


class SlackNotifier(IssueObserver):
    def __init__(self, channel: str):
        self.channel = channel

    def update(self, issue: Issue, changed_fields: Dict[str, Any]) -> None:
        # In a real implementation, this would send a Slack message
        print(f"Sending Slack notification to #{self.channel}:")
        print(f"Issue '{issue.title}' has been updated:")
        for field, changes in changed_fields.items():
            print(f"- {field}: {changes['old']} → {changes['new']}")


class LoggingObserver(IssueObserver):
    def update(self, issue: Issue, changed_fields: Dict[str, Any]) -> None:
        # In a real implementation, this would write to a log file
        print(f"[LOG] Issue {issue.title} updated at {issue.updated_at}:")
        for field, changes in changed_fields.items():
            print(f"[LOG] {field}: {changes['old']} → {changes['new']}") 