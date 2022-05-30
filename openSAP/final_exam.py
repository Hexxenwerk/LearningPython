from random import randrange


def word_list() -> list:
    with open('5_letter_words.txt', 'r') as file:
        return [word.strip() for word in file.readlines()]


def random_word(words: list) -> str:
    return words[randrange(0, len(words))]


def is_real_word(guess: str, words: list) -> bool:
    return guess in words


def check_guess(guess: str, word: str) -> str:
    result = ''
    found = []
    for index, character in enumerate(guess):
        if character == word[index]:
            result += 'X'
            found.append(character)
        elif character in word and character not in found:
            result += 'O'
            if word.count(character) < guess.count(character):
                found.append(character)
        else:
            result += '_'
    return result


def next_guess(words: list) -> str:
    guess = input('Please enter a guess: ').lower()
    while not is_real_word(guess, words):
        print("That's not a real word!")
        guess = input('Please enter a guess: ').lower()
    return guess


def play() -> None:
    won = False
    words = word_list()
    word = random_word(words)
    for _ in range(6):
        guess = next_guess(words)
        print(check_guess(guess, word))
        if guess == word:
            won = True
            break
    if won:
        print('You won!')
    else:
        print('You lost!')
        print(f'The word was: {word}')


play()
