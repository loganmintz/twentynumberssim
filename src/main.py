import math
import random
from boards import generate_board
import strategy as strategy_module
import concurrent.futures
import time
import click
import importlib

def run_simulation_chunk(start, end, max_num, max_rounds, num_pregen_positions, strategy):
    score = 0
    for _ in range(start, end):
        if strategy(generate_board(max_num, max_num, num_pregen_positions), max_num, max_rounds, num_pregen_positions) != []:
            score += 1
    return score

@click.command()
@click.argument('strategy_function')
def main(strategy_function):
    score = 0
    num_simulations = 1000000
    max_num = 1000
    max_rounds = 20
    num_pregen_positions = 0
    num_threads = 10
    chunk_size = num_simulations // num_threads

    print(f"Running {num_simulations} simulations")

    start_time = time.time()

    strategy = getattr(strategy_module, strategy_function)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(run_simulation_chunk, i * chunk_size, (i + 1) * chunk_size, max_num, max_rounds, num_pregen_positions, strategy)
            for i in range(num_threads)
        ]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            score += future.result()
            print(f"{(i + 1) * chunk_size} simulations done")
            print(f"Progress: {((i + 1) * chunk_size / num_simulations) * 100:.2f}%")


    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{score} successful games for {num_simulations}, {score/num_simulations*100}% chance!")
    print(f"Calculation time: {elapsed_time:.2f} seconds")
    print(f"Simulations per second: {num_simulations / elapsed_time:.2f}")

if __name__ == "__main__":
    main()