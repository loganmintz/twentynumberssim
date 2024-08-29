import math
import random

def box_muller(mean=0, std_dev=25, max_num=1000) -> int:
    ''' Standard Normal variate using Box-Muller transform: https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
    '''
    u = 1 - random.random()
    v = random.random()
    z = math.sqrt(-2.0 * math.log(u)) * math.cos(2.0 * math.pi * v)
    return abs(min(round(z * std_dev + mean), max_num))


def generate_board(max_num, max_rounds, num_pregen_positions) -> list:
    ''' Generate a board with normalized random numbers filled in at randomly generated positions.
    '''
    new_board = [-1 for _ in range(max_rounds)]
    pos_range = max_num / max_rounds
    numbers = random.sample(range(1, max_rounds+1), num_pregen_positions)
    numbers = sorted(numbers)
    for num in numbers:
        mean = (num * pos_range) - (pos_range / 2)
        std_dev = pos_range / 2
        #not super confident in the following. For now, I shifted everything to the 0 in order to avoid going over 1000 a lot
        new_board[num-1] = box_muller(mean, std_dev, max_num) 
    return new_board
