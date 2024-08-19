
# Developer : Kira Ash Stephenson (Solaas Ashen Onslaught)
# Description : The node class is used for modders to help manipulate the game.
#               Nodes are what fill the board in the game of Scalable Pentago.


class Node:
    """Nodes are what fill the board.  They hold states that are either empty or assigned to a player.
    This class can also be used to easily mod the game if they so wish.  To do so, add new properties to this
    class, define new methods that manipulate those properties inside the ScalablePentago class, and configure
    the gameplay_loop and gameplay_start methods in the ScalablePentago class to account for modifications."""

    def __init__(self, state):
        """Creates an instance of a node with the passed state."""
        self.__state = state

    def get_state(self):
        """Gets the current state of the node."""
        return self.__state

    def set_state(self, new_state):
        """Sets the state to the passed value."""
        self.__state = new_state
