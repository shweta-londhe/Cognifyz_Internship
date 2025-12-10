def reverse_string(text: str) -> str:
    """Return the reversed version of the given string."""
    return text[::-1]


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    reversed_text = reverse_string(user_input)
    print("Reversed String:", reversed_text)
