def check_password_strength(password: str) -> str:
    length_ok = len(password) >= 8
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(not ch.isalnum() for ch in password)

    score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])

    if score == 5:
        return "Strong Password"
    elif score >= 3:
        return "Medium Strength Password"
    else:
        return "Weak Password"


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result = check_password_strength(pwd)
    print(result)
