import random

from phrasehunter.phrase import Phrase


class Game():

    name = input('Please enter your name to continue:  ')

    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase('Every cloud has a silver lining'),
            Phrase('Happiness depends upon ourselves'),
            Phrase('A safe pair of hands'),
            Phrase('A turn up for the books'),
            Phrase('Act of God'),
            Phrase('Alive and Kicking'),
            Phrase('Old is gold'),
            Phrase('Fight the good fight'),
            Phrase('Game is up'),
            Phrase('keep your distance'),
            Phrase('Once in a blue moon'),
            Phrase('Rise and Shine'),
            Phrase('The apple of my eye'),
            Phrase('Think out of box'),
            Phrase('Twenty four seven')
        ]

        self.current_phrase = self.random_phrase_selector()
        self.guesses = [' ']

    def random_phrase_selector(self):
        return self.phrases[random.randint(0, 14)]

    def welcome(self):
        welcome = '<<<+++--- Phrase Hunter ---+++>>>'
        print('\n')
        print('*'*len(welcome))
        print(welcome)
        print('*'*len(welcome), '\n')

    def start_game(self):
        self.welcome()
        print(f'Hey {self.name}, ready for fun?', '\nYou got this!')
        while self.missed < 5 and not self.current_phrase.check_phrase_completion(self.guesses):
            print(f'\n\nNumber of wrong guesses: {self.missed}')
            self.current_phrase.display(self.guesses)
            player_guess = self.get_guess()
            self.guesses.append(player_guess)
            if not self.current_phrase.check_guess(player_guess):
                self.missed += 1

        self.game_over()
        self.again()

    def get_guess(self):
        guess = input('\nYour Guess:  ').lower()
        return guess

    def game_over(self):
        if self.missed == 5:
            print("="*30)
            print(f"\nOh no! Better luck next time {self.name}!\n")
            print("="*30)
        else:
            print("\nYou're such a Gamer!")
            print("="*30)
            print(f"\nCongrats, you've guessed the word {self.name}!\n")
            print("="*30)

    def again(self):
        option = input(
            'Would you like to go again? Press "y" to cotinue or any other key to quit:  ').lower()
        if option == 'y':
            self.__init__()
            self.start_game()
        else:
            print(f'---Thank You {self.name}, Have a great day!---')
