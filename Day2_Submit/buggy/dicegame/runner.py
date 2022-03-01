from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)


    # def reset(self):
    #     self.round = 1
    #     self.wins = 0
    #     self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        round = 1
        wins = 0
        losses = 0
        running = True
        while running == True:

            runner = cls()


            print("Round {}\n".format(round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins = wins + 1
                c = c + 1



            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                losses = losses + 1
                c = c



            print("Wins: {} Loses {}".format(wins, losses))
            round = round + 1



            if wins == 3:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
            if losses == 3:
                print("Good lord, you lost....")

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == 'Y':
                running = True
            else:
                print("Thanks for playing!")
                running = False
