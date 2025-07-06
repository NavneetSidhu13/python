import random 
number = random.randint(1, 5) # type: ignore # Random number between 1 and 100
guess = int(input("Guess a number between 1 and 5: "))
if guess == number:
    print("Congratulations! You guessed the number correctly.")
else:
    print(f"Sorry, the correct number was {number}. Better luck next time!")
