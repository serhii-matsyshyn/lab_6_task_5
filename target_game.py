""" Game 'Target'

Description of the game:
The player sees a playing field on which 9 letters.
The player's task is to find as many words
on the playing field as possible,
which consist of four or more letters.
Each letter can occur in a word as many times
as it occurs on the playing field.
Each word must contain a central letter.
"""

from typing import List
import random
import string


def generate_grid() -> List[List[str]]:
    """ Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]

    :return: Grid for the game
    :rtype: List[List[str]]
    """

    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    game_grid = [alphabet[number:number+3] for number in range(0, 9, 3)]

    return game_grid


def get_words(f: str,
              letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    pass


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str],
                        letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    """
    Displays and records the result.txt file
    of the game results
    """
    pass


if __name__ == '__main__':
    print(generate_grid())
