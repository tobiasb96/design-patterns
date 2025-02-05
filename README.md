# Design Patterns Challenges

This repository contains implementations of various design pattern challenges to demonstrate SOLID principles and common design patterns in Python.

## Project Structure

```
design-patterns/
├── src/
│   ├── challenge1/  # Bug Tracker with Dynamic Notifications
│   ├── challenge2/  # Document Converter System
│   ├── challenge3/  # Refactored Customer Manager
│   ├── challenge4/  # Legacy Payment Gateway Integration
│   └── challenge5/  # Web Request Handler Extension
└── tests/          # Corresponding test files for each challenge
```

## Setup

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a new virtual environment and install dependencies:
```bash
uv init
uv sync
```

## Running Tests

To run all tests:
```bash
uv pytest
```

To run tests with coverage:
```bash
uv pytest --cov=src tests/
```

## Challenges

1. **Bug Tracker with Dynamic Notifications**: Implementation of the Observer pattern for a bug tracking system.
2. **Document Converter System**: Factory pattern implementation for document conversion.
3. **Customer Manager Refactoring**: Example of applying Single Responsibility Principle.
4. **Legacy Payment Gateway Integration**: Adapter pattern implementation.
5. **Web Request Handler Extension**: Decorator pattern implementation.

## Development

- Each challenge is contained in its own module under the `src` directory
- Tests for each challenge are in the corresponding test files under the `tests` directory
- Code follows PEP 8 style guide and is formatted using Black