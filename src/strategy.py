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



def strategy_a(board, max_num, max_rounds, num_pregen_positions) -> list:
    result = board  # init result

    nums = random.sample(range(max_num), max_rounds-num_pregen_positions)

    for num in nums:
        div = num / (max_num / max_rounds)
        target_idx = math.floor(div)
        new_target = -1
       
        current = result[target_idx]  # successful simple case
        
        if current == -1:
            result[target_idx] = num
            continue

        if current < num:  # look for empty field upper
            search_range = range(target_idx + 1, max_rounds)
            for i in search_range:
                if result[i] == -1:  # found new candidate
                    new_target = i
                    break
                elif result[i] > num:  # only higher numbers upper...
                    break
        else:  # search for empty field lower
            search_range = reversed(range(0, target_idx))
            for i in search_range:
                if result[i] == -1:
                    new_target = i
                    break
                elif result[i] < num:
                    break

        if new_target == -1:  # no legitimate place found
            return []
        result[new_target] = num

    return result