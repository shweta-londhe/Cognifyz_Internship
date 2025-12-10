def is_palindrome(text: str) -> bool:
    """Return True if the string is a palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    user_input = input("Enter a word: ")

    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not a Palindrome")
