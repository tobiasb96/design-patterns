"""Challenge 1: Bug Tracker with Dynamic Notifications.

This module implements a bug tracking system using the Observer pattern to notify
multiple stakeholders when an issue's status changes.
"""

from .issue import Issue, IssueObserver, IssueStatus
from .observers import EmailNotifier, LoggingObserver, SlackNotifier

__all__ = [
    "EmailNotifier",
    "Issue",
    "IssueObserver",
    "IssueStatus",
    "LoggingObserver",
    "SlackNotifier",
]
