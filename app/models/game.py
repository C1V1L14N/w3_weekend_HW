from app.models.selection import *

class Game():
    # def __init__(self, player_1, player_2):
        
                            
    def play_game(player_1, player_2):
        if player_1.move == Selection.ROCK and player_2.move == Selection.PAPER:
            return f"{player_2.name} wins! Paper smothers Rock!"

        elif player_1.move == Selection.ROCK and player_2.move == Selection.SCISSORS:
            return f"{player_1.name} wins! Rock smashes Scissors!"

        elif player_1.move == Selection.PAPER and player_2.move == Selection.ROCK:
            return f"{player_1.name} wins! Paper smothers Rock!"

        elif player_1.move == Selection.PAPER and player_2.move == Selection.SCISSORS:
            return f"{player_2.name} wins! Scissors slice Paper!"

        elif player_1.move == Selection.SCISSORS and player_2.move == Selection.PAPER:
            return f"{player_1.name} wins! Scissors slice Paper!"

        elif player_1.move == Selection.SCISSORS and player_2.move == Selection.ROCK:
            return f"{player_2.name} wins! Rock smashes Scissors!"

        elif player_1.move == player_2.move:
            return "Ooooh, it's a draw!"




    


        