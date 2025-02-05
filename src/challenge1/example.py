from .issue import Issue, IssueStatus
from .observers import EmailNotifier, SlackNotifier, LoggingObserver


def main():
    # Create a new issue
    bug = Issue(
        title="Login Page Error",
        description="Users cannot log in using their Google accounts"
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
    print("\n=== Assigning the issue ===")
    bug.assign_to("alice@example.com")

    print("\n=== Updating status to IN_PROGRESS ===")
    bug.update_status(IssueStatus.IN_PROGRESS)

    print("\n=== Reassigning the issue ===")
    bug.assign_to("bob@example.com")

    print("\n=== Marking as resolved ===")
    bug.update_status(IssueStatus.RESOLVED)

    # Detach an observer
    print("\n=== Detaching QA team ===")
    bug.detach(qa_email)

    print("\n=== Closing the issue ===")
    bug.update_status(IssueStatus.CLOSED)


if __name__ == "__main__":
    main() 