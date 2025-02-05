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
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def send(self, message: str, **kwargs):
        pass


class EmailNotifier(Notifier):
    def __init__(self, host: str, **kwargs):
        super().__init__(**kwargs)
        self.host = host

    def send(self, message: str, subject_line: str, **kwargs):
        print(f"Email sent: {subject_line} - {message}")


class SlackNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send(self, message: str, **kwargs):
        print(f"Slack Message sent: {message}")


class CustomerDataManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_customer(self, customer_data: dict):
        print(f"Saving customer data: {customer_data} to {self.file_path}")


class CustomerManagerRefactored:

    def __init__(self, notifier: Notifier, data_manager: CustomerDataManager):
        self.data_manager = data_manager
        self.notifier = notifier

    def process_customer(self, customer_data) -> None:
        self.data_manager.create_customer(customer_data)
        self.notifier.send("Welcome")


if __name__ == "__main__":
    customer_info = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
    notifier = EmailNotifier(host="hubspot.com")
    data_manager = CustomerDataManager("customer.txt")
    manager = CustomerManagerRefactored(notifier, data_manager)
    manager.process_customer(customer_data=customer_info)

