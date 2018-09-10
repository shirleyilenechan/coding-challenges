# The move sequence is represented by a string, and the character moves[i] represents its ith move.
# Valid moves are R (right), L (left), U (up), and D (down). If the robot returns
# to the origin after it finishes all of its moves, return true. Otherwise, return false.


def judgeCircle(moves):
    if moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D"):
        return True
    return False
