import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
stages = hangman_art.stages
lives = len(stages)-1

chosen_word = list(random.choice(word_list))
display = list("_" * len(chosen_word))

print(f"{hangman_art.logo}\n\n")
print(f"\n\t\t\t\t\033[93m{"".join(display)}\033[0m\n")

while chosen_word != display and lives > 0:
    guess = input("Guess a letter: ").lower()

    guessed = False
    guessed_already = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            guessed = True
            if display[i] == guess:
                guessed_already = True
            display[i] = guess

    if not guessed:
        print(f"Sorry, \"{guess}\" is not here. You lose a life.")
        lives -= 1
    elif guessed_already:
        print(f"You have already guessed letter \"{guess}\".")
    else:
        print("Correct!")

    print(f"\n\t\t\t\t\033[93m{"".join(display)}\033[0m")
    print(f'''
                \033[92m******************************
                        {lives} live(s) left
                ******************************\033[0m''')
    print(f"{stages[lives]}\n\n\n\n")

if lives == 0:
    print("\033[95m==================== YOU LOSE ====================\033[0m")
    print(f"{"".join(chosen_word)} was correct word.")
else:
    print("\033[95m==================== YOU WIN! ====================\033[0m")
