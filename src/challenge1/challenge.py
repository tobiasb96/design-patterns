"""
Challenge 1: Bug Tracker with Dynamic Notifications

Requirements:
------------
1. Create a core Issue class representing a bug report
2. Build a mechanism that allows multiple observers to subscribe to status updates
3. Observers should be able to be added or removed at runtime
4. The system must notify all subscribers when an issue is updated

Hints:
------
- Consider implementing a custom event or signal system (Observer pattern)
- Ensure that the Issue class itself remains focused on tracking bug details (SRP)
- Your design should allow for additional observers (e.g., logging, email notifications) 
  to be added later without modifying the Issue class

Example Test Cases to Consider:
-----------------------------
1. Test issue creation with default values
2. Test attaching and detaching observers
3. Test that observers are notified when issue status changes
4. Test that observers are notified when issue is assigned
5. Test that no notification is sent when value doesn't change
6. Test multiple observers receiving notifications
"""

# Implement your solution here 