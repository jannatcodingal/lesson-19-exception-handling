while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                if age % 2 == 0:
                    print("Your age is even.")
                else:
                    print("Your age is odd.")
                break
            else:
                print("Age cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")