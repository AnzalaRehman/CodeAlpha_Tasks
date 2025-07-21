import random

# List of words
words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)

guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print(f"❌ Wrong! Tries left: {tries}")

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

if tries == 0:
    print(f"💀 Game Over! The word was: {word}")
