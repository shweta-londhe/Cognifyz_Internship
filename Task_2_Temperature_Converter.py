def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", c_to_f(c))

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", f_to_c(f))

    else:
        print("Invalid choice.")
