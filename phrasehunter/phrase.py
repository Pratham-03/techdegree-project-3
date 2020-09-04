from string import ascii_lowercase


class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, letters):
        for letter in self.phrase:
            if letter in letters:
                print(f'{letter}', end=' ')
            elif letter not in letters:
                print('_', end=' ')

    def check_guess(self, guess):
        characters = ascii_lowercase
        if len(guess) != 1 or guess not in characters:
            print("\nERROR: Oh no, that's not a valid guess. Please try again...")
        elif guess in self.phrase:
            return True
        else:
            return False

    def check_phrase_completion(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        else:
            return True
