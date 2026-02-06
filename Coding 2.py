import random
# generate a secret number between 1 and 10
secret_number = random.randint(1, 10)

# keep asking until the guess is correct
while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break