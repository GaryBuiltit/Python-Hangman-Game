import random
import hangman_art as art
import hangman_words as words

word_list = words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)

# print(f'Pssst, the solution is {chosen_word}.')

guessed = []

display = []

for _ in range(word_length):
  display += "_"

print(f'Word has {word_length} letters')
print('Good Luck!')
print(art.stages[lives])

print(f"{' '.join(display)}\n\n")

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess not in guessed:
    guessed += guess
    # print(guessed)
  else:
    print(f'{guess} was already chosen!')
    continue

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f'Sorry no {guess}')
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"You lose! Word was {chosen_word}")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(art.stages[lives])
