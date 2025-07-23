import random

words = ["apple", "banana", "cherry", "grapes", "orange"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!\n")

while attempts > 0:
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {display_word}")
    
    if "_" not in display_word:
        print(" Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess.")
        attempts -= 1
        guessed_letters.append(guess)

    print(f"Attempts left: {attempts}\n")

if "_" in display_word:
    print(f"Game over! The word was: {secret_word}")
