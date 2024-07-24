"""
This module handles the words of the crossword puzzle.
Like loading the word, selecting orientation and pos.

__AUTHOR__ = "Kriti Bhatnagar" and "Anand Maurya"
"""

from pickle import load
from typing import Literal
from os.path import join
from random import choice


"""
All the methods are anonymous and in a class
to avoid assigning and 
calling each function for all the 3 difficulties.
"""


class Words:
    def __init__(self, difficulty: Literal["Easy", "Medium", "Hard"]) -> None:
        """
        This initializes words for a particular difficulty.

        @param: difficulty : Literal["Easy", "Medium", "Hard"]
            The difficulty of the words.
        """
        self.words = self.__get_words(difficulty)
        self.words = self.__select_orientation(self.words)

    def __get_words(self, difficulty: Literal["Easy", "Medium", "Hard"]) -> list[str]:
        """
        This gets the words based on the difficulty given.

        @param: difficulty : Literal["Easy", "Medium", "Hard"]
            The difficulty of words to get.

        @returns: list[str]
            The list of the words of the particular difficulty.
        """
        words_path = join("Assets", "WordData.dat")
        with open(words_path, "rb") as words:
            words = load(words)
            return words[difficulty]

    def __select_orientation(self, word_list: list[str]) -> dict[str, str]:
        """
        This selects the orientation for each word in a word list.

        @param: word_list : list[str]
            The list of the words.

        @returns: dict[str, str]
            The dict of the word mapped with its orientation.
        """
        ORIENTATIONS = [
            "HorizontalLeft",
            "HorizontalRight",
            "HorizontalUp",
            "HorizontalDown",
            "LeftUp",
            "LeftDown",
            "RightUp",
            "RightDown",
        ]
        return {word: choice(ORIENTATIONS) for word in word_list}

    def __select_pos(
        self, word_list: dict[str, str]
    ) -> dict[str, list[tuple[int, int]]]:
        """
        This assigns all the letter of all the words to a valid pos on the grid.

        @param: word_list : dict[str, str]
            The word mapped to its orientation.

        @returns: dict[str, list[tuple[int, int]]]
            The word mapped to all the positions on the grid of all its letters.
        """
        pos_dict = {}
        for word, orientation in word_list.items():
            # TODO: Figure this shit out.
            pos = None
            pos_dict[pos] = (word, orientation)
        return pos_dict
