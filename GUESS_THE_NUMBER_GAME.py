import random 
secret_num = random.randint(1, 100)
guess = 0
num_guesses = 0

while guess != secret_num :
    num_guesses += 1 
    guess= int(input("Enter a guess between  1 and 100: "))
    if guess < secret_num:
            print("Your guess is too low, try again")
    elif guess  > secret_num :
            print( "Your Guess is too high, try again")

    else:
            print(f"congratulations your guessed the mumber in {num_guesses} guesse!")