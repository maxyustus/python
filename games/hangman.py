import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
length_word = len(chosen_word)
user_lives = 5
end_of_game = False

display = []

for _ in range(length_word):
    display += '_'

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(length_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        user_lives -= 1
        if user_lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
