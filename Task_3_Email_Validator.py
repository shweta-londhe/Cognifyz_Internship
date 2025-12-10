def is_valid_email(email: str) -> bool:
    """Return True if email is valid based on basic rules."""
    
    if "@" not in email:
        return False
    
    if "." not in email.split("@")[-1]:
        return False

    if " " in email:
        return False
    
    if email[0] in "._@":
        return False

    return True


if __name__ == "__main__":
    user_email = input("Enter your email: ")

    if is_valid_email(user_email):
        print("Valid Email")
    else:
        print("Invalid Email")
