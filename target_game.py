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

    alphabet = list(string.ascii_uppercase)*3
    random.shuffle(alphabet)
    game_grid = [alphabet[number:number+3] for number in range(0, 9, 3)]

    return game_grid


def get_words(filename: str,
              letters: List[str]) -> List[str]:
    """ Reads the file f.
    Checks the words with rules and returns a list of words.

    :param filename: All words filename
    :type filename: str
    :param letters: Letters to check
    :type letters: List[str]
    :return: A list of words that can be found in list of letters
    :rtype: List[str]
    """
    with open(filename) as file:
        all_words = [line.rstrip() for line in file.readlines()]

    return get_words_list(letters, all_words)


def get_words_list(letters: List[str],
                   words_from_dict: List[str]) -> List[str]:
    """ Checks the words with rules and returns a list of words.

    :param letters: Letters to check
    :type letters: List[str]
    :param words_from_dict: List with words from dict
    :type words_from_dict: List[str]
    :return: A list of words that can be found in list of letters
    :rtype: List[str]
    """
    output_words = []
    for word_from_dict in words_from_dict:
        if (len(word_from_dict) >= 4) and (letters[4] in word_from_dict):
            word_from_dict_list = list(word_from_dict)
            for letter in letters:
                if letter in word_from_dict_list:
                    word_from_dict_list.remove(letter)
            if not word_from_dict_list:
                output_words.append(word_from_dict)

    return output_words


def get_user_words() -> List[str]:
    """ Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.

    :return: list with words
    :rtype: List[str]
    """
    words_input = input("Enter the words (lowercase) separated by space: ")
    return list(set(words_input.split()))


def get_pure_user_words(user_words: List[str],
                        letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """ Checks user words with the rules and returns list of those words
    that are not in dictionary.

    :param user_words: User words to check
    :type user_words: List[str]
    :param letters: Letters to check
    :type letters: List[str]
    :param words_from_dict: List with words from dict
    :type words_from_dict: List[str]
    :return: returns list of those words
    that are not in dictionary
    :rtype: List[str]
    """

    output_words = []
    words_in_string = get_words_list(letters, words_from_dict)
    for user_word in user_words:
        if (len(user_word) >= 4) and (letters[4] in user_word) and (user_word not in words_in_string):
            output_words.append(user_word)

    return output_words


def print_both(line: str, file):
    """ Prints result to console and to file

    :param line: Line to print
    :type line: Str
    :param file: File to write to
    :type file: file
    """
    print(line)
    print(line, file=file)


def results():
    """
    Displays and records the result.txt file
    of the game results
    """
    letters = generate_grid()
    print(letters[0], letters[1], letters[2], sep='\n')

    letters_list = letters[0] + letters[1] + letters[2]
    correct_words = get_words("en", letters_list)

    words_input = get_user_words()

    with open("result.txt", 'w') as file:
        print_both("Correct words you have found: ", file)
        for word_input in words_input:
            if word_input in correct_words:
                print_both(word_input, file)

        print_both("Incorrect words you have found: ", file)
        for word in get_pure_user_words(words_input,
                                        letters_list,
                                        correct_words):
            print_both(word, file)

        print_both("More words that can be found: ", file)
        for word in set(correct_words)-set(words_input):
            print_both(word, file)


if __name__ == '__main__':
    results()
