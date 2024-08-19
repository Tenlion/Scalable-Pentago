
import ScalablePentago

# Explaining the game.
print("Welcome to Scalable Pentago!  It's Pentago but the board can scale up to 26x26 nodes, there" + '\n' +
      "can be 26 players, the winning sequence can go up to the board's length, and the board has" + '\n' +
      "the ability to split into a number of sub-boards that can be produced with a base of 4.  As" + '\n' +
      "for rules, please follow any directions given for inputs; read carefully.  A good GENERAL" + '\n' +
      "rule is to ensure your inputs are an integer value above 0.  In addition, the sub-boards are" + '\n' +
      "numbered from top-to-down and left-to-right (starting at 1, not 0); horizontal first, then vertical.  Have fun!")
print('\n' + "Press ENTER to define your game's board.")
input()

# Making the game.
game = ScalablePentago.ScalablePentago()
game.gameplay_start()
