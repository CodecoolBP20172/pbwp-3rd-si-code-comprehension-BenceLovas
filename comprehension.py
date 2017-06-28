import random  # Import random module's library, binds the module name to the module object in the local namespace

guessesTaken = 0  # Initialize gussesTaken variable with 0 value

print('Hello! What is your name?')  # Prints to console
myName = input()  # Prompts user for his/her name and stores the input as a variable

number = random.randint(1, 20)  # Assign secret random number between 1-20(inclusively) to a variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Prints concatinated strins

while guessesTaken < 6:  # Prompts user for guesses while guessesTaken is less then 6, or guess is right
    print('Take a guess.')  # Print
    guess = input()  # Prompts user for input and assigns it to guess variable
    guess = int(guess)  # Reassigns variable with its casted previous value

    guessesTaken += 1  # Increments guessesTaken by 1

    if guess < number:  # If user's guess is lower than the secret number
        print('Your guess is too low.')  # Print

    if guess > number:  # If user's guess is higher than the secret number
        print('Your guess is too high.')  # Print

    if guess == number:  # If the user guessed right
        break  # Terminates loop

if guess == number:  # If user's guess equals the secret number
    guessesTaken = str(guessesTaken)  # Reassigns variable with its casted previous value
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Prints guesses taken

if guess != number:  # If guess is not equal to the secret number
    number = str(number)  # Reassigns variable with its casted previous value
    print('Nope. The number I was thinking of was ' + number)  # Reveals secret number
