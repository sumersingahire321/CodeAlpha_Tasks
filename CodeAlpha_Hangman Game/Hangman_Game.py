import random

# Step 1: Create a list of 5 predefined words
words = ["python", "apple", "tiger", "chair", "house"]

# Step 2: Choose a random word
word = random.choice(words)

# Step 3: Create empty list to store guessed letters
guessed_letters = []

# Step 4: Set maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.\n")

# Step 5: Game loop
while wrong_guesses < max_wrong:

    display_word = ""

    # Show current progress
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses, "\n")
    else:
        print("✅ Correct guess!\n")

# If player loses
if wrong_guesses == max_wrong:
    print("💀 Game Over! The word was:", word)
