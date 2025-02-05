"""
Challenge 5: Extend a Basic Web Request Handler

Requirements:
------------
Create one or more decorators to extend the RequestHandler so that:
1. Every request is logged before processing
2. An authentication check is performed before the request is handled

Your solution should allow you to "wrap" a RequestHandler with these additional
behaviors without modifying the original class.

The following class CANNOT be modified:
"""

class RequestHandler:
    def handle_request(self, request):
        # Process the incoming request
        print(f"Handling request: {request}")


"""
Your Task:
---------
1. Create decorator class(es) that implement the same interface as RequestHandler
2. Add logging functionality that records each request before processing
3. Add authentication checking that verifies the request before processing
4. Ensure decorators can be applied in any order

Example Test Cases to Consider:
-----------------------------
1. Test that original RequestHandler works unchanged
2. Test logging decorator captures request details
3. Test authentication decorator checks credentials
4. Test both decorators can be used together
5. Test decorators work in different orders
6. Test error handling in decorators
"""

# Implement your solution here 