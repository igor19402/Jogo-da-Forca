# Write your code here
import random
print("H A N G M A N")
words_guess = ('python', 'java', 'kotlin', 'javascript')
word_choice = random.choice(words_guess)
word_choice_set = set(word_choice)
hint_word = len(word_choice) * "-".split()
tries = 8
letters_attempts = []

while True:
    while True:
        option = input("Type 'play' to play the game, 'exit' to quit:")
        if option != "exit" and option != "play":
            continue
        else:
            break
    if option == "exit":
        break
    while tries >= 1:
        while True:
            print()
            print("".join(hint_word))
            letter = input("Input a letter: ")
            if len(letter) > 1:
                print("You should input a single letter")
            elif not letter.islower():
                print("Please enter a lowercase English letter")
            else:
                break
        if letter in letters_attempts:
            print("You've already guessed this letter")
        elif letter not in word_choice_set:
            print("That letter doesn't appear in the word")
            tries -= 1
        elif letter in word_choice_set and letter not in letters_attempts:
            for i in range(len(word_choice)):
                if word_choice[i] == letter:
                    hint_word[i] = letter
        if "".join(hint_word) == word_choice:
            print("".join(hint_word))
            print("You guessed the word!")
            print("You survived!")
            print()
            break
        if tries == 0:
            print("You lost!")
            print()
            break
        letters_attempts.append(letter)

# print()
# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")

# if word == word_choice:
#     print("You survived!")
# else:
#     print("You lost!")
