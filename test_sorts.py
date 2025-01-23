"""Oussama Abouyahia Worked with Ryan Debbarh and Houssam Maarouf
Lab07 Slow Sorting
 03/03/2024"""
import random
from slow_sorts import selection_sort, insertion_sort, bubble_sort
from asymp_printout import asymp_printout


def run_trials(sort_function, sizes, num_trials):
    op_counts = []
    for size in sizes:
        total_ops = 0
        for _ in range(num_trials):
            arr = [random.randint(0, size) for _ in range(size)]
            ops = sort_function(arr)
            total_ops += ops
        average_ops = total_ops / num_trials
        op_counts.append((size, average_ops))
    return op_counts


if __name__ == "__main__":
    sizes = [100, 200, 300, 400, 500]
    num_trials = 10

    selection_sort_times = run_trials(selection_sort, sizes, num_trials)
    insertion_sort_times = run_trials(insertion_sort, sizes, num_trials)
    bubble_sort_times = run_trials(bubble_sort, sizes, num_trials)

    print("Selection Sort:")
    asymp_printout(selection_sort_times)

    print("\nInsertion Sort:")
    asymp_printout(insertion_sort_times)

    print("\nBubble Sort:")
    asymp_printout(bubble_sort_times)
