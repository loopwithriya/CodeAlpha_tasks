#This is my version of the Hangman game for CodeAlpha internship 
#I learned how to use loops , conditions and strings in python
import random

# Step 1: Define a list of 5 predefined words
word_list = ['banana', 'dog', 'zebra', 'sad', 'lucky']

# Step 2: Randomly choose a word from the list
secret_word = random.choice(word_list)

# Step 3: Initialize variables
guessed_letters = []
attempts = 6

print("🎮 Let's play Hangman Game Buddy!")
print("You can make only 6 mistakes.Good luck Buddy!")
print(f"You have {attempts} incorrect guesses allowed Play Safe!.\n")

# Step 4: Main game loop
while attempts > 0:
    display_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'

    print("Word:", ' '.join(display_word))

    if display_word == secret_word:
        print("\n🎉 AURA INFINITY!! CHALLENGE CONQUERED")
        break

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter only a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter Buddy. Try a new one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Great Job Buddy! You Guessed a correct letter.\n")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.\n")

# Step 5: Check for loss
if display_word != secret_word:
    print(f"\n😢 Game Over! The word was: {secret_word}")
