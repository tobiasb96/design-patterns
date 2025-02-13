"""Challenge 4: Integrate a Legacy Payment Gateway.

Requirements:
------------
Design and implement an adapter that wraps LegacyPaymentGateway so that it conforms
to the modern interface (i.e., provides a process(amount) method).
Then, demonstrate its usage with the Checkout class.

The following classes CANNOT be modified:
"""

# Legacy Payment Gateway (cannot be modified)
class LegacyPaymentGateway:
    def make_payment(self, value) -> None:
        pass


# Modern system interface (cannot be modified)
class Checkout:
    def __init__(self, payment_gateway) -> None:
        self.payment_gateway = payment_gateway

    def complete_order(self, amount) -> None:
        self.payment_gateway.process(amount)


"""
Your Task:
---------
1. Create an adapter class that makes LegacyPaymentGateway work with the Checkout class
2. The adapter should implement the process(amount) method expected by Checkout
3. Internally, the adapter should use LegacyPaymentGateway's make_payment method

Example Test Cases to Consider:
-----------------------------
1. Test adapter correctly forwards the payment amount
2. Test adapter works with the Checkout class
3. Test error handling in the adapter
4. Test that the original LegacyPaymentGateway behavior is preserved
"""

# Implement your solution here
