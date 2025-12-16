def filter_above_threshold(numbers, threshold):
    """Return values greater than the given threshold."""
    return [num for num in numbers if num > threshold]


if __name__ == "__main__":
    print("Enter numbers separated by spaces:")
    user_numbers = list(map(int, input().split()))

    th = int(input("Enter threshold value: "))

    filtered = filter_above_threshold(user_numbers, th)

    print("Numbers above threshold:", filtered)
