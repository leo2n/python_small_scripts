"""
@author: leo
a set for count game
Usage:
    from countgame import CountGame
    x = CountGame()
    x.count_times(x, y)
"""

from random import randrange

class CountGame:
    """
    Just for fun : )
    """
    def __init__(self):
        pass

    def count_times(self, x, y):
        """
        choose a number between x and y, count 100 times, sorted by times.      
        """
        count_list = []
        for i in range(100):
            result = randrange(x, y)
            count_list.append(result)
        count_set = set(count_list)
        count_dict = {index: count_list.count(index) for index in count_set}

        for frequency in sorted(count_dict, key=lambda x: count_dict[x], reverse=True):
            print("{} ----- {}".format(frequency, count_dict[frequency]))
