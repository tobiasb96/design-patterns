"""Test cases for Challenge 3: CustomerManager Refactoring.

These tests should pass both before and after your refactoring,
ensuring that the functionality remains the same while the code structure improves.
"""

import os

import pytest

from src.challenge3.customer_manager import CustomerManager


@pytest.fixture
def customer_data():
    return {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "address": "123 Main St",
    }


@pytest.fixture
def clean_customer_file():
    # Setup: ensure the file doesn't exist
    if os.path.exists("customers.txt"):
        os.remove("customers.txt")
    yield
    # Teardown: clean up the file
    if os.path.exists("customers.txt"):
        os.remove("customers.txt")


def test_customer_initialization(customer_data) -> None:
    manager = CustomerManager(customer_data)
    assert manager.customer_data == customer_data


def test_save_customer_creates_file(customer_data, clean_customer_file) -> None:
    manager = CustomerManager(customer_data)
    manager.save_customer()
    assert os.path.exists("customers.txt")


def test_save_customer_writes_data(customer_data, clean_customer_file) -> None:
    manager = CustomerManager(customer_data)
    manager.save_customer()

    with open("customers.txt") as f:
        content = f.read().strip()

    assert str(customer_data) in content


def test_process_customer_workflow(customer_data, clean_customer_file, capsys) -> None:
    manager = CustomerManager(customer_data)
    manager.process_customer()

    # Check if file was created
    assert os.path.exists("customers.txt")

    # Check if email was "sent"
    captured = capsys.readouterr()
    assert "Sending welcome email to alice@example.com" in captured.out
    assert "Processing customer data..." in captured.out


# Additional tests to consider implementing:
# 1. Test customer data validation
# 2. Test email format validation
# 3. Test handling of missing customer data
# 4. Test file append functionality (multiple customers)
# 5. Test error handling for file operations
