from datetime import datetime

import pytest

from src.challenge1.issue import Issue, IssueStatus
from src.challenge1.observers import EmailNotifier, LoggingObserver, SlackNotifier


@pytest.fixture
def issue():
    return Issue(
        title="Test Bug",
        description="This is a test bug",
    )


@pytest.fixture
def email_observer():
    return EmailNotifier("dev@example.com")


@pytest.fixture
def slack_observer():
    return SlackNotifier("bugs")


@pytest.fixture
def logging_observer():
    return LoggingObserver()


def test_issue_creation(issue) -> None:
    assert issue.title == "Test Bug"
    assert issue.description == "This is a test bug"
    assert issue.status == IssueStatus.OPEN
    assert isinstance(issue.created_at, datetime)
    assert issue.updated_at == issue.created_at
    assert issue.assigned_to is None


def test_attach_observer(issue, email_observer) -> None:
    issue.attach(email_observer)
    assert email_observer in issue._observers


def test_detach_observer(issue, email_observer) -> None:
    issue.attach(email_observer)
    issue.detach(email_observer)
    assert email_observer not in issue._observers


def test_multiple_observers(issue, email_observer, slack_observer, logging_observer, capsys) -> None:
    # Attach all observers
    issue.attach(email_observer)
    issue.attach(slack_observer)
    issue.attach(logging_observer)

    # Update status
    issue.update_status(IssueStatus.IN_PROGRESS)

    # Check that all observers were notified
    captured = capsys.readouterr()
    output = captured.out

    assert "Sending email to dev@example.com" in output
    assert "Sending Slack notification to #bugs" in output
    assert "[LOG] Issue Test Bug updated" in output


def test_status_update_notification(issue, email_observer, capsys) -> None:
    issue.attach(email_observer)
    issue.update_status(IssueStatus.IN_PROGRESS)

    captured = capsys.readouterr()
    output = captured.out

    assert "status: IssueStatus.OPEN → IssueStatus.IN_PROGRESS" in output


def test_assignment_notification(issue, slack_observer, capsys) -> None:
    issue.attach(slack_observer)
    issue.assign_to("alice")

    captured = capsys.readouterr()
    output = captured.out

    assert "assigned_to: None → alice" in output


def test_no_notification_on_same_value(issue, email_observer, capsys) -> None:
    issue.attach(email_observer)

    # Assign the same status
    issue.update_status(IssueStatus.OPEN)

    captured = capsys.readouterr()
    assert captured.out == ""  # No notification should be sent
