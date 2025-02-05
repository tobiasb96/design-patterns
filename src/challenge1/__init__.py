"""
Challenge 1: Bug Tracker with Dynamic Notifications

This module implements a bug tracking system using the Observer pattern to notify
multiple stakeholders when an issue's status changes.
"""

from .issue import Issue, IssueStatus, IssueObserver
from .observers import EmailNotifier, SlackNotifier, LoggingObserver

__all__ = [
    'Issue',
    'IssueStatus',
    'IssueObserver',
    'EmailNotifier',
    'SlackNotifier',
    'LoggingObserver',
] 