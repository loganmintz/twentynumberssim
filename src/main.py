"""20 Numbers challange is a challange where someone draws 20 numbers without repetitions from <0, 999>, one by one, and tries to sort them on go.
Example of such a game which interested me: https://vm.tiktok.com/ZGJCKHjDa/
This experiment is supposed to check possibility of success in this challange.
We assume that someones strategy is to put numbers wrt their placements from uniform distribution.
We can imagine 20 buckets (start, end), where each start and end are lower and upper bound for drawed numbers.
If the bucket is filled, we will search next free closest bucket without runining the sorting order.
F.e buckets [<0, 50), <50, 100), ..., <950, 1000)] for even distribution (50 numbers for each bucket).
This implementation gave me 6456 and 6457 successes in two tries with 100 milion simulations, so the chance is ~ 0.00646%.
I've found reddit thread with similar results: https://www.reddit.com/r/theydidthemath/comments/11rm4ka/comment/jc9x0xf/?utm_source=share&utm_medium=web2x&context=3
"""
import math
import random
from boards import generate_board
from strategy import strategy_a

def main():
    score = 0
    num_simulations = 500000

    max_num = 1000
    max_rounds = 20
    num_pregen_positions = 0
    
    print(f"Running {num_simulations} simulations")
          
    for _ in range(num_simulations):
        if strategy_a(generate_board(max_num, max_num, num_pregen_positions), max_num, max_rounds, num_pregen_positions) != []:
            score += 1
        if _ % 20000 == 0:
            print(f"{_} simulations done")

    print(f"{score} successful games for {num_simulations}, {score/num_simulations*100}% chance!")


if __name__ == "__main__":
    main()