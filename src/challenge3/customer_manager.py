"""Challenge 3: Refactor a Monolithic CustomerManager.

Your Task:
---------
Refactor this class to adhere to the Single Responsibility Principle (SRP) by separating:
- Customer data handling
- File persistence
- Email notifications

Consider using dependency injection to decouple these responsibilities.
"""
from abc import ABC, abstractmethod


class CustomerManager:
    def __init__(self, customer_data) -> None:
        self.customer_data = customer_data  # Handles in-memory customer info
        self.file_path = "customers.txt"

    def save_customer(self) -> None:
        # Save customer data to a file
        with open(self.file_path, "a") as f:
            f.write(str(self.customer_data) + "\n")

    def send_welcome_email(self) -> None:
        # Simulate sending a welcome email
        pass

    def process_customer(self) -> None:
        # Process customer data (e.g., validation, formatting)
        self.save_customer()
        self.send_welcome_email()


# This code needs to be refactored following SRP
# Implement your refactored solution below

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def __init__(self, email_address:str, **kwargs):
        super().__init__(**kwargs)
        self.email_address = email_address

    def send(self, message: str):
        print(f"Email sent: {message}")


class SlackNotifier(Notifier):
    def __init__(self, slack_account_number: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send(self, message: str):
        print(f"Slack Message sent: {message}")


class NotifierFactory(ABC):
    @abstractmethod
    def create_notifier(self, customer_data):
        pass


class EmailNotifierFactory(NotifierFactory):
    @abstractmethod
    def create_notifier(self, customer_data):
        return EmailNotifier(email_address=customer_data.email_address)


class SlackNotifierFactory(NotifierFactory):
    @abstractmethod
    def create_notifier(self, customer_data):
        return SlackNotifier(slack_account_number=customer_data.slack_account_number)


class CustomerWelcomer(ABC):
    def __init__(self, notifier_factory: NotifierFactory):
        self.notifier_factory = notifier_factory

    @abstractmethod
    def welcome(self, name: str):
        pass

class CustomerEmailWelcomer(CustomerWelcomer):
    def __init__(self, notifier_factory: EmailNotifierFactory):
        super().__init__(notifier_factory)

    def welcome(self, customer_data):
        email_message = f"...{customer_data.name}..."
        notifier = self.notifier_factory.create_notifier(customer_data)
        notifier.send(email_message)


class CustomerSlackWelcomer(CustomerWelcomer):
    def __init__(self, notifier_factory: SlackNotifierFactory):
        super().__init__(notifier_factory)

    def welcome(self, customer_data):
        slack_message = f"...SLACK_SPECIFIC_STUFF...{customer_data.name}..."
        notifier = self.notifier_factory.create_notifier(customer_data)
        return notifier.send(slack_message)

class CustomerSaver(ABC):
    @abstractmethod
    def save(self, customer_data):
        pass

class CustomerFileSaver(CustomerSaver):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, customer_data):
        with open(self.filepath, "a") as f:
            f.write(str(customer_data) + "\n")

class CustomerDbSaver(CustomerSaver):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def save(self, customer_data):
        print(f"Saving to db using {self.connection_string}")

class CustomerManagerRefactored:
    def __init__(self, welcomer: CustomerWelcomer, saver: CustomerSaver):
        self.welcomer = welcomer
        self.saver = saver

    def process_customer(self, customer_data):
        self.saver.save(customer_data=customer_data)
        self.welcomer.welcome(name=customer_data.name)


if __name__ == "__main__":
    data = {...}
    n_factory = EmailNotifierFactory()
    welcomer = CustomerEmailWelcomer(n_factory)
    saver = CustomerDbSaver("connection_string")
    customer_manager = CustomerManagerRefactored(welcomer, saver)
    customer_manager.process_customer(data)