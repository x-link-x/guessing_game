correct_guess = 4

guess = input("Guess a number: ")

while guess:

    if int(guess) == correct_guess:
        print("Correct")
        break
    else:
        print("Try again")

    guess = input("Guess a number: ")