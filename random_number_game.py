import random

number_to_guess = random.randint(1,10)

for turns in range(6):
    print("Enter your guess here!")
    guess = input()
    if guess == number_to_guess:
        print("Congratulations, you have guessed correctly")
        break
    elif guess < number_to_guess:
        print ("The number you are looking for is bigger than your guess")
    else:
        print("The number you are looking for is smaller than your guess")
else:
    print("You have run out of guesses, you lose, the correct answer was: " + str(number_to_guess))