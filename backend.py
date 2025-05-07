# backend.py
"""
Backend logic for the app.
This file contains stub implementations of backend functions
like sign_up and log_in for demonstration purposes.
"""

def sign_up(username: str, email: str, password: str) -> bool:
    # Example stub function - in real app you'd add user to DB
    print(f"Sign up request - username: {username}, email: {email}")
    # You could add validation and persistence here
    return True  # Return True if sign up succeeded

def log_in(email: str, password: str) -> bool:
    # Example stub function - in real app you'd check credentials
    print(f"Log in request - email: {email}")
    # Simulate successful login if password is 'password123' else fail
    if password == "password123":
        return True
    else:
        return False

