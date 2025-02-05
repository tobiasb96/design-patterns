"""Challenge 3: Refactor a Monolithic CustomerManager.

Your Task:
---------
Refactor this class to adhere to the Single Responsibility Principle (SRP) by separating:
- Customer data handling
- File persistence
- Email notifications

Consider using dependency injection to decouple these responsibilities.
"""


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
