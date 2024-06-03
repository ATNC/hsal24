import random
import time
import cProfile
import pstats

from bbst import BBST


def generate_random_dataset(size):
    return [random.randint(0, 10000) for _ in range(size)]


def measure_complexity():
    num_datasets = 100

    total_insert_time = 0
    total_delete_time = 0
    total_search_time = 0

    dataset = generate_random_dataset(100)

    avl_tree = BBST()

    start_time = time.time()
    for key in dataset:
        avl_tree.insert(key)
    total_insert_time += time.time() - start_time

    start_time = time.time()
    for key in dataset:
        avl_tree.delete(key)
    total_delete_time += time.time() - start_time

    for key in dataset:
        avl_tree.insert(key)

    start_time = time.time()
    for key in dataset:
        avl_tree.find(key)
    total_search_time += time.time() - start_time

    avg_insert_time = total_insert_time / num_datasets
    avg_delete_time = total_delete_time / num_datasets
    avg_search_time = total_search_time / num_datasets

    print(f"Avg. Insert Time: {avg_insert_time:.6f} seconds")
    print(f"Avg. Delete Time: {avg_delete_time:.6f} seconds")
    print(f"Avg. Search Time: {avg_search_time:.6f} seconds")
    print()


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.runcall(measure_complexity)
    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
