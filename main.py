def run_average_calculator():
    numbers = []

    print("Simple Average Calculator")
    print("Commands: + to add number, = to show average, q to quit")

    while True:
        command = input("\nEnter command (+, =, q): ").strip().lower()

        if command == "+":
            value = input("Enter a number: ").strip()
            try:
                num = float(value)
                numbers.append(num)
                print(f"Added: {num}")
            except ValueError:
                print("That is not a valid number. Please try again.")

        elif command == "=":
            if not numbers:
                print("No numbers added yet.")
            else:
                avg = sum(numbers) / len(numbers)
                print(f"Numbers: {numbers}")
                print(f"Average: {avg}")

        elif command == "q":
            print("Goodbye.")
            break

        else:
            print("Invalid command. Use +, =, or q.")
