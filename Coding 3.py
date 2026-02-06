def collatz(n):
    if n % 2 == 0:
        result = n // 2
        print(result)
        return result
    else:
        result = 3 * n + 1
        print(result)
        return result


# Main program with input validation
while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


# Step counter
steps = 0

while num != 1:
    num = collatz(num)
    steps += 1

print(f"It took {steps} steps to reach 1.")