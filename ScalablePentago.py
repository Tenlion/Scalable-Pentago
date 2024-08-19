
# Developer Name : Kira Ash Stephenson (Solaas Ashen Onslaught)
# Description : Welcome to Scalable Pentago!  It's Pentago but the board can scale up to 26x26 nodes, there
#               can be 26 players, the winning sequence can go up to the board's length, and the board has
#               the ability to split into a number of sub-boards that can be produced with a base of 4.  As
#               for rules, please follow any directions given for inputs; read carefully.  A good GENERAL
#               rule is to ensure your inputs are an integer value above 0.  In addition, the sub-boards are
#               numbered from top-to-down and left-to-right (starting at 1, not 0); horizontal first, then vertical.
#               Have fun!


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


class ScalablePentago:
    """Used to create instances of scalable versions of the game Pentago."""

    def __init__(self):
        """Develops an instance of a Pentago board and properties needed for the game."""

        # Obtaining the sub_board length.
        self.__sub_board_length = self.obtain_sub_board_length()

        # Obtaining the sub_board_number and board_length.
        number_and_length = self.obtain_subnumber_and_boardlength()
        self.__sub_board_number = number_and_length[0]
        self.__board_length = number_and_length[1]

        # Obtaining the length required to win the game.
        self.__winning_length = self.obtain_winning_length()

        # Obtaining the player count.
        self.__player_count = self.obtain_player_count()

        # Creating a string to dictate the number of players and their identity in the game.
        # Filling the player string with lettered values by converting the ASCII values to characters
        # and adding one to ensure that a new value is created off of the end of the string.
        self.__players = "A"
        for player in range(self.__player_count - 1):
            self.__players += chr(ord(self.__players[-1]) + 1)

        # Creating an x_label for the board.
        # Filling the x_label with English capital characters up to the board's length.
        # The board's length goes up to a maximum of 26, which is the maximum amount of letters in the English alphabet.
        self.__x_label = "A"
        for number in range(self.__board_length - 1):
            self.__x_label += chr(ord(self.__x_label[-1]) + 1)

        # Creating a board using a matrix.  Each row is a new list.
        # In addition, we also define what values are an empty space in the board using the blank property.
        self.__board = []
        self.__blank = "#"
        for row in range(self.__board_length):
            new_row = []
            self.__board.append(new_row)

            # Creating nodes for each column in the newly made rows.
            for column in range(self.__board_length):

                # Makes a node with the blank value and appends the node to the current row's values.
                node = Node(self.__blank)
                self.__board[row].append(node)

    def get_board_value_of_letter(self, letter):
        """Returns the integer value of where a letter would be on the board's dimensions."""

        # Checks if the letter is lowercase. (This check goes first because humans are innately lazy.)
        # If true, return the integer value of the letter minus 97; ninety-seven is a constant due to ASCII.
        if letter.islower():
            return ord(letter) - 97

        # Checks if the letter is uppercase.
        # If true, return the integer value of the minus 65; sixty-five is a constant due to ASCII.
        if letter.isupper():
            return ord(letter) - 65

    def obtain_sub_board_length(self):
        """RECURSIVE METHOD : Returns the sub_board_length as determined by user input.  If the input
        is not acceptable, the method will keep asking for the sub_board_length."""

        # Printing out a question for the user to answer.
        print("What is the length of the sides of your Pentago's sub-boards?" + '\n' +
              "The number must be greater than 1.")

        # Trying to obtain the input.
        # If the input is not of the correct data type, throw an error and recur.
        try:
            length_of_sub_board = int(input())
        except ValueError:
            print("ERROR : Please input an integer value.")
            return self.obtain_sub_board_length()

        # Check if the sub_board_length is of a lower value than 1.
        # If true, send out an error explaining what's wrong and recur.
        if length_of_sub_board < 2:
            print("ERROR : Please input a number that is greater than 1 for your sub-board length.")
            return self.obtain_sub_board_length()

        # BASE CASE : If the above check was false, return the length of the sub-board.
        return length_of_sub_board

    def obtain_subnumber_and_boardlength(self):
        """RECURSIVE METHOD : Returns the sub-board count and the game board's length if the user input
        for the sub-board power is deemed acceptable."""

        # Printing out a question for the user to answer.
        print('\n' + "The number of sub-boards in this version of Pentago is 4 to the power of X." + '\n' +
              "If X were 1, then 4 sub-boards are made; a value of 2 would equate to 16 sub-boards." + '\n' +
              "The number must be greater than 0 and can't push the sides of the game board over 26." + '\n' +
              "To determine the game board's length, use this formula: sub_board_length * sqrt(4^X)" + '\n' +
              "So, what is your X?")

        # Trying to obtain the input.
        # If the input is not of the correct data type, throw an error and recur.
        try:
            sub_board_power = int(input())
        except ValueError:
            print("ERROR : Please input an integer value.")
            return self.obtain_subnumber_and_boardlength()

        # Calculating the game board's length using the number of sub-boards and the sub-board length.
        number_of_sub_boards = 4 ** sub_board_power
        length_of_board = int(self.__sub_board_length * (number_of_sub_boards ** 0.5))

        # The below checks determine if the input received was an acceptable value.
        # If ANY are true, the method will recur and display a message that explains why it's recurring.

        # SUB-BOARD POWER CHECK : Check if the inputted X is greater than 0.
        if sub_board_power < 1:
            print("ERROR : Your X power is not greater than 0.")
            return self.obtain_subnumber_and_boardlength()

        # LENGTH OF BOARD CHECK : Check if the board length is greater than 100.
        if length_of_board > 26:
            print("ERROR : Your board length is too large." + '\n' +
                  "Your Board Length : " + str(length_of_board))
            return self.obtain_subnumber_and_boardlength()

        # BASE CASE : If the above checks equate false,
        # the sub-board count and the board's length will be returned in a list.
        return [number_of_sub_boards, length_of_board]

    def obtain_winning_length(self):
        """RECURSIVE METHOD : Returns the winning length if the user input is an acceptable value for the length.
        If it's not, the method will recur and ask for new input."""

        # Printing out a question for the user to answer.
        print('\n' + "How many nodes in a row will equate to a win in your game?" + '\n' +
              "The winning length can't be greater than the board length and can't be lower than 2." + '\n' +
              "Your board length, which is calculated by sub_board_length * sqrt(4^X), is: " + str(self.__board_length))

        # Trying to obtain the input.
        # If the input is not of the correct data type, throw an error and recur.
        try:
            length_to_win = int(input())
        except ValueError:
            print("ERROR : Please input an integer value.")
            return self.obtain_winning_length()

        # The below checks determine if the input received was an acceptable value.
        # If ANY are true, the method will recur and display a message that explains why it's recurring.

        # 1st WINNING LENGTH CHECK : Check if the winning length is greater than the board length.
        if length_to_win > self.__board_length:
            print("ERROR : Your winning length is greater than the board's length.  That's not feasible.")
            return self.obtain_winning_length()

        # 2nd WINNING LENGTH CHECK : Check if the winning length is lower than 2.
        if length_to_win < 2:
            print("ERROR : Your winning length is too short.  Values lower than 2 are not acceptable.")
            return self.obtain_winning_length()

        # BASE CASE : If the above checks equate false, return length_to_win.
        return length_to_win

    def obtain_player_count(self):
        """RECURSIVE METHOD : Will return the inputted player count if the value has been deemed acceptable.
        If not, the method will recur until an acceptable value has been received."""

        # Declaring variables that will be used in the checks.
        nodes_in_board = self.__board_length * self.__board_length
        player_maximum = int(nodes_in_board / self.__winning_length)

        # Printing out a question for the user to answer.
        print('\n' + "How many players will be playing?" + '\n' +
              "Player count must be greater than 1, lower than your game's player maximum, and lower than 27." + '\n' +
              "The nodes in the board is the board length multiplied by itself." + '\n' +
              "The player maximum is the nodes in the board divided by the winning length (truncated)." + '\n' +
              "The nodes in the board is the board length multiplied by itself." + '\n' +
              "Nodes in Board : " + str(nodes_in_board) + '\n' +
              "Player Maximum : " + str(player_maximum))

        # Trying to obtain the input.
        # If the input is not of the correct data type, throw an error and recur.
        try:
            number_of_players = int(input())
        except ValueError:
            print("ERROR : Please input an integer value.")
            return self.obtain_player_count()

        # The below checks determine if the input received was an acceptable value.
        # If ANY are true, the method will recur and display a message that explains why it's recurring.

        # 1st PLAYER COUNT CHECK : Check if the number of players is lower than 2.
        if number_of_players < 2:
            print("ERROR : The player count is too low.  The player count can NOT be lower than 2.")
            return self.obtain_player_count()

        # 2nd PLAYER COUNT CHECK : Check if the number of players is higher than 26.
        if number_of_players > 26:
            print("ERROR : The player count is too high.  The player count can NOT be higher than 26.")
            return self.obtain_player_count()

        # 3rd PLAYER COUNT CHECK : Check if the number of players is greater than the player maximum.
        if number_of_players > player_maximum:
            print("ERROR : Your player count is too high.  The player count can NOT be higher than the total number of nodes in" + '\n' +
                  "the board divided by the winning length.  If it is, it's impossible for any player to conceivably win" + '\n' +
                  "before the board fills up since players HAVE to place marbles down on their turn.")
            return self.obtain_player_count()

        # BASE CASE : If the above checks equate false, return the number of players that will be used for the game.
        return number_of_players

    def obtain_row_and_column(self):
        """RECURSIVE METHOD : Will return the row and column input values as a list where row is index 0 and
        column is index 1.  This will only happen if the input has been deemed valid.  ALSO, THIS RETURNS THE
        COLUMN AS AN INTEGER!  Column is inputted as a character, but is flipped to an integer."""

        # Trying to obtain row input.
        # If the input is not of the correct data type, throw an error and recur.
        try:
            print("Row of Marble Position : ", end='')
            row_of_marble = int(input())
        except ValueError:
            print("ERROR : Please input an integer value.")
            return self.obtain_row_and_column()

        # ROW CHECK : Checking if the row input is within the board's length.
        if (row_of_marble < 0) or (row_of_marble > self.__board_length - 1):
            print("ERROR : Your input for row is not within the board's boundaries.")
            return self.obtain_row_and_column()

        # Obtaining column input.
        print("Column of Marble Position : ", end='')
        col_of_marble = input()

        # 1st COLUMN CHECK : Checking if the column is an english letter.
        if not col_of_marble.isalpha():
            print("ERROR : Your input for column is not alphanumeric.  Please input a letter.")
            return self.obtain_row_and_column()

        # 2nd COLUMN CHECK : Checking if the column input is within the board's length.
        col_of_marble = self.get_board_value_of_letter(col_of_marble)
        if (col_of_marble < 0) or (col_of_marble > self.__board_length - 1):
            print("ERROR : Your input for column is not within the board's boundaries.")
            return self.obtain_row_and_column()

        # POSITION CHECK : Checking if the specified position is filled already.
        if self.__board[row_of_marble][col_of_marble].get_state() != self.__blank:
            print("ERROR : The position is already filled.  Please select a new position.")
            return self.obtain_row_and_column()

        # BASE CASE : If the above checks equate false, return the row and column values as a list.
        return [row_of_marble, col_of_marble]

    def obtain_sub_board(self):
        """RECURSIVE METHOD : Return the number of the sub-board that the player wishes to rotate, but only if
        it's of an acceptable value."""

        # Trying to obtain the input.
        # If the input is not of the correct data type, throw an error and recur.
        try:
            print("Sub-Board to Rotate : ", end='')
            board_to_rotate = int(input())
        except ValueError:
            print("ERROR : Please input an integer value.")
            return self.obtain_sub_board()

        # Checking if the chosen board exists or not.
        # If the board doesn't exist, recur and explain that the input was not acceptable.
        if (board_to_rotate < 1) or (board_to_rotate > self.__sub_board_number):
            print("ERROR : The sub-board value must be greater than 0 and less than " + str(self.__sub_board_number) + ".")
            return self.obtain_sub_board()

        # BASE CASE : If the above check equates false, return board_to_rotate.
        return board_to_rotate

    def obtain_rotation_direction(self):
        """RECURSIVE METHOD : Will return the rotation direction that a sub_board should rotate if the input is
        of an acceptable value."""

        # Printing a question for the player to answer.
        print("Clockwise or Counter Clockwise? Input 'C' for clockwise and 'A' for counter clockwise.", end='')

        # Obtaining input from the player.
        rotation_direction = input()

        # Creating a list of acceptable answers.
        list_of_acceptabilities = ['c', 'C', 'a', 'A']

        # Looping through the acceptibility list to see if the input was an acceptability.
        # If it was, flip found_acceptability to True.
        found_acceptability = False
        for character in list_of_acceptabilities:
            if character == rotation_direction:
                found_acceptability = True
                break

        # BASE CASE : If an acceptability was found, return the rotation_direction.
        # Otherwise, recur the method and ask for new input.
        if found_acceptability:
            return rotation_direction
        else:
            print("ERROR : Your input was neither 'c', 'C', 'a', or 'A' for the rotation's direction.")
            return self.obtain_rotation_direction()

    def check_direction(self, direction, row, column, length_to_check, state_of_player):
        """RECURSIVE METHOD : Returns true if a winning sequence was achieved in the desired direction.
        Returns false otherwise."""

        # BASE CASE : If the winning length is 0, this means the player won.
        if length_to_check == 0:
            return True

        # Switch to dictate which direction logic we will be using to change the row and column values.
        match direction:

            # North
            case 0:
                row -= 1

            # Northeast
            case 1:
                row -= 1
                column += 1

            # East
            case 2:
                column += 1

            # Southeast
            case 3:
                row += 1
                column += 1

            # South
            case 4:
                row += 1

            # Southwest
            case 5:
                row += 1
                column -= 1

            # West
            case 6:
                column -= 1

            # Northwest
            case 7:
                row -= 1
                column -= 1
            case _:
                print("Something went wrong with check_direction.")

        # Defining the board limits to prevent boundary errors.
        board_maximum = self.__board_length - 1
        board_minimum = 0

        # BASE CASE: Checking if the boundary limits have been crossed.
        # If so, return false.
        if (row > board_maximum) or (row < board_minimum):
            return False
        if (column > board_maximum) or (column < board_minimum):
            return False

        # BASE CASE : Checking if the state of the node is blank or does NOT equal the player state.
        # If either are true, return False as that means the direction is pointless to pursue.
        state_to_check = self.__board[row][column].get_state()
        if (state_to_check == self.__blank) or (state_to_check != state_of_player):
            return False

        # Decrementing the length_to_check by 1 since we've now checked a node.
        length_to_check -= 1

        # Recur with the new row, column, and length_to_check values.
        return self.check_direction(direction, row, column, length_to_check, state_of_player)

    def check_for_player_win(self, row, column, winning_list, state_of_node):
        """Checks the list of players on the current node to see if a winning sequence can be achieved from it.
        After the check has been made, the winning list will hold true values for the players that won."""

        # Loop to determine how many times win scenarios need to be checked.
        # This is based on the player count since we need to see if a change to the board has caused any player to win.
        # Ties are possible, so we have to check every player.
        for player in range(self.__player_count):

            # Checking if the player state is equal to the state of the node.
            # If so, proceed to check the directions around the node for a winning sequence.
            player_state = self.__players[player]
            if player_state == state_of_node:

                # Loop that checks all 8 directions around a node for a winning sequence.
                for direction in range(8):

                    # Checking to see if the current player has won in any of the directions.
                    # If so, break out of this loop and continue to the next player.
                    if winning_list[player]:
                        break

                    # Check if the current direction has a winning sequence for the player.
                    # Then assign the result, whether true or false, to the winning_list.
                    player_has_won = self.check_direction(direction, row, column, self.__winning_length - 1, player_state)
                    winning_list[player] = player_has_won

    def get_game_state(self, marble_sub_board, rotated_sub_board):
        """Returns a list of booleans that is the same size as the players string for the game.  Players who have
        won will have their corresponding index value set to true inside the list.  As an example, if Player C has won,
        then index 2 inside the list will be set to true."""

        # Creating a list of booleans set to false that holds a length equivalent to the player count in the game.
        players_that_won = [False] * self.__player_count

        # Checking if the passed sub_boards are the same.
        # If they are, we only need to check one of them.  If not, we check both.
        if marble_sub_board == rotated_sub_board:
            boards_to_check = [marble_sub_board]
        else:
            boards_to_check = [marble_sub_board, rotated_sub_board]

        # Loop that goes through each board to check for a winning condition for every player.
        for sub_board in range(len(boards_to_check)):

            # Obtaining the upper left corner position of the current sub_board.
            sub_board_corner = self.sub_board_corner_position(boards_to_check[sub_board])
            corners_row = int(sub_board_corner[0])
            corners_column = int(sub_board_corner[1])

            # Nested loop to locate the current node to be checked for a player win.
            for row in range(self.__sub_board_length):
                sub_board_row = corners_row + row
                for column in range(self.__sub_board_length):
                    sub_board_column = corners_column + column

                    # Check to see if the node is NOT empty.
                    # If it's not empty, check to see if ANY of the players have won starting at that node.
                    # If it's empty, move on to the next node.
                    state_to_check = self.__board[sub_board_row][sub_board_column].get_state()
                    if state_to_check != self.__blank:

                        # This will alter the contents of the players_that_won variable to indicate which
                        # players have won in the game.  Those that have won, will have their values set to true
                        # inside the list.  Player A is index 0, player B is index 1, and so on and so forth.
                        self.check_for_player_win(sub_board_row, sub_board_column, players_that_won, state_to_check)

        # Returning the list of players who have won.
        return players_that_won

    def is_board_full(self):
        """Checking to see if the board is full of marbles.  Will return true if it's full, false otherwise."""

        # Creating a boolean for return; method is looking for a flip to true.
        board_is_full = False

        # Counting out the number of nodes in the board that have non-defaulted states.
        counted_nodes = 0
        for row in range(self.__board_length):
            for column in range(self.__board_length):
                if self.__board[row][column].get_state() != self.__blank:
                    counted_nodes += 1

        # Checking if the counted nodes value is equal to the number of nodes within the board.
        # If this is true, flip the boolean we made at the start to True.
        number_of_nodes_in_board = self.__board_length * self.__board_length
        if counted_nodes == number_of_nodes_in_board:
            board_is_full = True

        # Return the result of the boolean.
        return board_is_full

    def sub_board_corner_position(self, sub_board):
        """Returns a list containing the upper left corner position of the desired sub-board.
        The first value in the list is the row position.  The second is the column position."""

        # Creating an empty list to return the row and column position of the sub board for later.
        upper_left_position = []

        # Determining the relative multiplier for both the row and column of the desired sub_board position.
            # This is achieved by first calculating the number of sub_boards present in a horizontal and vertical sequence.
            # We do this to ensure the multiplier is always relative to the board size.  Afterwards, we use the relative factor
            # to calculate the multipliers.
        divisions_in_lateral_sequence = self.__board_length / self.__sub_board_length
        row_multiplier = int(sub_board / divisions_in_lateral_sequence)
        column_multiplier = int(sub_board % divisions_in_lateral_sequence) - 1

        # Checking if the sub_board number modulo-ed by the divisions in sequence is equivalent to 0.  This is an indication
        # that the sub board might be on the edge of the game board, so we need to make sure there are no off-by-one errors
        # in this circumstance (multiplier can go over the board's boundaries otherwise).
        if (sub_board % divisions_in_lateral_sequence) == 0:
            column_multiplier = divisions_in_lateral_sequence - 1
            row_multiplier -= 1

        # Using the calculated multipliers, determine the position of both the row and column of the sub-board's
        # upper left corner is.  We want the upper left corner to make sifting through the sub-board's contents easier
        # when rotating the board in the future (center position logic is more annoying to work with here).
        sub_board_row_position = row_multiplier * self.__sub_board_length
        sub_board_column_position = column_multiplier * self.__sub_board_length

        # Add the positions to the empty list made at the start of the method.
        upper_left_position.append(sub_board_row_position)
        upper_left_position.append(sub_board_column_position)

        # Return the upper left position of the sub-board.
        return upper_left_position

    def rotate(self, sub_board, rotation):
        """Rotates a given sub_board in the desired direction."""

        # Obtaining the upper left corner position of the passed sub_board.
        sub_board_corner = self.sub_board_corner_position(sub_board)
        corners_row = int(sub_board_corner[0])
        corners_column = int(sub_board_corner[1])

        # THE MOST IMPORTANT VARIABLE
        # Determines how many nodes in a given sequence need to be rotated.  This will be subtracted in the while-loop
        # for each iteration because as we go down the rows, there will be fewer nodes in a row to rotate.
        # This always starts out as the sub_board's length minus 1 since the first node replaces the ending
        # node present in a lateral sequence.
        nodes_in_sequence_to_rotate = int(self.__sub_board_length - 1)

        # Determines how many rows we'll be going through inside the sub_board for rotation.  We don't need to
        # go through all of them since the rotation aspect will deal with half of them.  However, we do need a
        # value relative to the board's length.
            # We convert the calculation to an integer in case the sub_board_length is odd and we need to truncate
            # down 1; this is done since odd value boards generate a center point with one node which does not need
            # to be rotated.  Also, we don't want floating point values from the division since we need to use
            # the variable for looping.
        rows_to_rotate = int(self.__sub_board_length / 2)

        # Clockwise Rotation
        if (rotation == 'C') or (rotation == 'c'):

            # This loop determines the square in which nodes will be rotated.
            for row in range(rows_to_rotate):

                # This loop determines how many nodes are left in the square to be rotated.
                for node in range(nodes_in_sequence_to_rotate):

                    # Acquiring the position of the starting node of 4 to move and assigning the node to a variable.
                    node_row = corners_row + row
                    node_column = corners_column + node + row
                    node_to_move = self.__board[node_row][node_column]

                    # Calculating the two movements that are associated with the set of 4 nodes that will be rotated.
                        # Move 1 is calculated by getting the number of nodes that are left in a square's side to be
                        # rotated.  This number's starting value increases as we go through each square (the row).
                        # Move 2 is calculated by taking the total movement (nodes_in_sequence_to_rotate) and
                        # subracting it from Move 1.  Both moves operate as boundary checkers.
                    move_1 = ((corners_column + nodes_in_sequence_to_rotate) - node_column) + row
                    move_2 = nodes_in_sequence_to_rotate - move_1

                    # This loop will rotate 4 nodes within the square starting with the node that corresponds
                    # to the position of node_row and node_column.
                    for turn in range(4):

                        # Switch that determines which turn we are on during a rotation so that the
                        # previously calculated moves are applied correctly.  Case "_" is just in case something breaks.
                        match turn:
                            case 0:
                                new_node_row = node_row + move_2
                                new_node_column = node_column + move_1
                            case 1:
                                new_node_row = node_row + move_1
                                new_node_column = node_column - move_2
                            case 2:
                                new_node_row = node_row - move_2
                                new_node_column = node_column - move_1
                            case 3:
                                new_node_row = node_row - move_1
                                new_node_column = node_column + move_2
                            case _:
                                print("Something went wrong with rotation.")
                                new_node_row = 0
                                new_node_column = 0

                        # Moving a node without deleting the next one to be moved.
                            # Make a temp variable to store the future node to be moved, assign the found position
                            # to the node we are currently moving, and then assign node_to_move to the next node
                            # to be moved.
                        temp = self.__board[new_node_row][new_node_column]
                        self.__board[new_node_row][new_node_column] = node_to_move
                        node_to_move = temp

                        # Updating node_row and node_column to ensure switch-case logic doesn't falter with each turn.
                        node_row = new_node_row
                        node_column = new_node_column

                # After going through a row, we subtract 2 from the sequence of nodes to rotate.
                # We do this because the next square to rotate around will have a length that is 2 less in length.
                    # If we were to compare this to the last square, it would be like trimming the first and last node
                    # for each side of the square.
                nodes_in_sequence_to_rotate -= 2

        # Anti-Clockwise Rotation (Two comments denote the difference between clockwise rotation.)
        if (rotation == 'A') or (rotation == 'a'):
            for row in range(rows_to_rotate):
                for node in range(nodes_in_sequence_to_rotate):

                    node_row = corners_row + row
                    node_column = corners_column + node + row
                    node_to_move = self.__board[node_row][node_column]

                    # Flip the move logic in clockwise rotation and you get the moves below.
                    move_2 = ((corners_column + nodes_in_sequence_to_rotate) - node_column) + row
                    move_1 = nodes_in_sequence_to_rotate - move_2

                    # Flip the logic seen in clockwise rotation and you get the cases below.
                    for turn in range(4):
                        match turn:
                            case 0:
                                new_node_row = node_row + move_2
                                new_node_column = node_column - move_1
                            case 1:
                                new_node_row = node_row + move_1
                                new_node_column = node_column + move_2
                            case 2:
                                new_node_row = node_row - move_2
                                new_node_column = node_column + move_1
                            case 3:
                                new_node_row = node_row - move_1
                                new_node_column = node_column - move_2
                            case _:
                                print("Something went wrong with rotation.")
                                new_node_row = 0
                                new_node_column = 0

                        temp = self.__board[new_node_row][new_node_column]
                        self.__board[new_node_row][new_node_column] = node_to_move
                        node_to_move = temp

                        node_row = new_node_row
                        node_column = new_node_column

                nodes_in_sequence_to_rotate -= 2

    def print_board(self):
        """Prints out the current contents of the Pentago board."""

        # PART 1 : Print out the x_label, a corner space, and a line to separate the label from the board contents.

        # Printing upper left corner space for the board.
        print("  " + " ", end='')

        # Printing out the X label of the board that sits on the top.
        x_counter = 1
        for character in self.__x_label:

            # Print the column's designator and add a space.
            print(character + " ", end='')

            # Check if the x_counter is equivalent to the sub_board_length.
            # If true, reset the x_counter and print an extra space to help split the sub_boards columns.
            if x_counter == self.__sub_board_length:
                x_counter = 0
                print(" ", end='')

            # Accumulate the x_counter by 1 to ensure we're building up to another sub_board split.
            x_counter += 1

        # This print is to separate the x_label from the board's contents.
        print()



        # PART 2 : Print out the board contents and ensure the sub_boards are split from each other.

        # Printing out the Y label of the board and the contents of the Pentago board.
        y_counter = 1
        x_counter = 1
        for row in range(self.__board_length):

            # If the row value is below 10, print a space out before the row identifier is printed.
            # Otherwise, simply print the row identifier.
            if row < 10:
                print(" " + str(row) + " ", end='')
            else:
                print(str(row) + " ", end='')

            # Loop out the states of each node in the board and check for sub_board splitting.
            for column in range(self.__board_length):

                # Print out the current node and follow it with a space.
                print(self.__board[row][column].get_state() + " ", end='')

                # Check if the x_counter is equivalent to the sub_board_length.
                # If true, reset the x_counter and print an extra space to help split the sub_board columns.
                # Afterwards, accumulate the x_counter.
                if x_counter == self.__sub_board_length:
                    x_counter = 0
                    print(" ", end='')
                x_counter += 1

            # Check if the y_counter is equivalent to the sub_board_length.
            # If true, reset the y_counter and print an extra line to help split the sub_board rows.
            # Afterwards, accumulate the y_counter.
            if y_counter == self.__sub_board_length:
                y_counter = 0
                print()
            y_counter += 1

            # Print is placed here so that the next row of contents is placed on a new line.
            print()

    def sub_board_of_node(self, row, column):
        """Returns the sub_board number of where a node is currently at."""
        variable_1 = int(row / self.__sub_board_length) * (self.__board_length / self.__sub_board_length)
        variable_2 = int(column / self.__sub_board_length)

        return variable_1 + variable_2

    def gameplay_loop(self, player, marbled_board, rotated_board):
        """RECURSIVE METHOD : Will only return if there is at least one winner or the board is full.  The return
        ends the game.  Otherwise, the game will keep looping and asking for a player to take their turn.  The next
        player is called to make their turn at the end of this method.  A round in the game is reset by a check
        that looks to see if the current player is the last one in the list of players."""

        # Printing out the game board for all players to see.
        self.print_board()

        # Printing out whose turn it is.
        print("PLAYER " + self.__players[player] + "'S TURN")

        # Obtaining input for the marble's position, sub_board to rotate, and the rotation direction.
        row_and_column = self.obtain_row_and_column()
        board_to_rotate = self.obtain_sub_board()
        rotation_direction = self.obtain_rotation_direction()

        # Placing the marble onto the desired position and rotating the chosen sub_board in the specified direction.
        self.__board[row_and_column[0]][row_and_column[1]].set_state(self.__players[0])
        self.rotate(board_to_rotate, rotation_direction)

        # Calculating the sub_board that the marble was placed in.
        sub_board_of_marble = self.sub_board_of_node(row_and_column[0], row_and_column[1])

        # Obtaining a list of possible victors after the last turn's occurrence.
        possible_victors = self.get_game_state(marbled_board, rotated_board)

        # Looping through the list of possible victors to see if one of them achieved victory.
        # If a victory occurred, print out who won and flip the game_is_done variable.
        # Multiple winners can happen and this loop will print out a line for every winner.
        game_is_done = False
        for participant in range(len(possible_victors)):
            if possible_victors[participant]:
                print("Player " + self.__players[participant] + " is a winner!")
                game_is_done = True

        # BASE CASE : Checking if someone won in the above loop.
        # If this is true, then the game is over and it's time to end the recursion/game.
        if game_is_done:
            print("The game is now over!  I hope everyone had fun.  Rerun the program to play again. :)")
            return

        # BASE CASE : Checking if the board is full.
        # If it is, then the recursion/game is over as no more moves can be made.  Nobody wins in this case.
        if self.is_board_full():
            print("The board is full.  Nobody won.  Rerun the program to play again.")
            return

        # Checking if the current player is the last one in the round.
        # If this is the case, reset the round by setting the player's value to be before the first player's value.
        if self.__players[-1] == self.__players[player]:
            player = -1

        # Start the gameplay loop using the next player.
        self.gameplay_loop(player + 1, sub_board_of_marble, board_to_rotate)

    def gameplay_start(self):
        """RECURSIVE STARTER : This will begin the game by printing the board and asking for the first player to
        take their turn.  At the end of the method, recursion begins and turns constantly loop until a winner
        is claimed or the board is full."""

        # Printing out the game board for all players to see.
        self.print_board()

        # Printing out that it's the first player's turn.
        print("PLAYER " + self.__players[0] + "'S TURN")

        # Obtaining input for the marble's position, sub_board to rotate, and the rotation direction.
        row_and_column = self.obtain_row_and_column()
        board_to_rotate = self.obtain_sub_board()
        rotation_direction = self.obtain_rotation_direction()

        # Placing the marble onto the desired position and rotating the chosen sub_board in the specified direction.
        self.__board[row_and_column[0]][row_and_column[1]].set_state(self.__players[0])
        self.rotate(board_to_rotate, rotation_direction)

        # Calculating the sub_board that the marble was placed in.
        sub_board_of_marble = self.sub_board_of_node(row_and_column[0], row_and_column[1])

        # Start the gameplay loop using the next player.
        self.gameplay_loop(1, sub_board_of_marble, board_to_rotate)
