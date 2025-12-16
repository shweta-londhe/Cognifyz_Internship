def count_words(text: str) -> int:
    """Return number of words in a given string."""
    words = text.split()
    return len(words)


if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    total_words = count_words(user_input)
    print("Total Words:", total_words)
