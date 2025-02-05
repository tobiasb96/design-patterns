from .issue import Issue, IssueStatus
from .observers import EmailNotifier, LoggingObserver, SlackNotifier


def main() -> None:
    # Create a new issue
    bug = Issue(
        title="Login Page Error",
        description="Users cannot log in using their Google accounts",
    )

    # Create different types of observers
    dev_email = EmailNotifier("dev-team@example.com")
    qa_email = EmailNotifier("qa-team@example.com")
    slack = SlackNotifier("critical-bugs")
    logger = LoggingObserver()

    # Attach observers to the issue
    bug.attach(dev_email)
    bug.attach(qa_email)
    bug.attach(slack)
    bug.attach(logger)

    # Make some changes to the issue and watch the notifications
    bug.assign_to("alice@example.com")

    bug.update_status(IssueStatus.IN_PROGRESS)

    bug.assign_to("bob@example.com")

    bug.update_status(IssueStatus.RESOLVED)

    # Detach an observer
    bug.detach(qa_email)

    bug.update_status(IssueStatus.CLOSED)


if __name__ == "__main__":
    main()
