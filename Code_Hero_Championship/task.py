
import random
def roast_move(move):
  roasts = [
      f"Wow, '{move}' - bold choice... said no grandmaster ever.",
          f"'{move}' - aka the 'I give up' move.",
              f"Did '{move}' come from a chess book... for beginners?"
                ]
                  return random.choice(roasts)
                  def predict_loss(moves_left):
                    predictions = [
                        f"Checkmate in {moves_left}... if you don't resign sooner.",
                            f"You've got {moves_left} moves left - barely enough time to facepalm.",
                                f"Game over in {moves_left} moves - better call a timeout... for your ego."
                                  ]
                                    return random.choice(predictions)
                                    def pawn_pwnz():
                                      print("Welcome to PawnPwnz - your chess game just got ROASTED!")
                                        move = input("Enter your move: ")
                                          print(roast_move(move))
                                            moves_left = int(input("How many moves till checkmate (guess): "))
                                              print(predict_loss(moves_left))
                                              pawn_pwnz()
                                              ```
                              