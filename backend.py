def sign_up(username: str, email: str, password: str) -> bool:
    print(f"Sign up request - username: {username}, email: {email}")
    return True  

def log_in(email: str, password: str) -> bool:
    print(f"Log in request - email: {email}")
    if password == "password123":
        return True
    else:
        return False

