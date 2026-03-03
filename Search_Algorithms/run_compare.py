"""
Runs BFS and DFS on Missionaries & Cannibals and compares performance.
"""

import time
from missionaries_cannibals import MissionariesCannibals
from bfs_dfs import bfs, dfs


def main():
    problem = MissionariesCannibals()

    print("=== Missionaries and Cannibals Problem ===")

    # BFS
    start = time.time()
    sol_bfs, exp_bfs, frontier_bfs = bfs(problem)
    end = time.time()
    print("\n--- BFS ---")
    print("Solution:", sol_bfs)
    print("Nodes Expanded:", exp_bfs)
    print("Max Frontier Size:", frontier_bfs)
    print("Time:", round(end - start, 6), "sec")

    # DFS
    start = time.time()
    sol_dfs, exp_dfs, frontier_dfs = dfs(problem)
    end = time.time()
    print("\n--- DFS ---")
    print("Solution:", sol_dfs)
    print("Nodes Expanded:", exp_dfs)
    print("Max Frontier Size:", frontier_dfs)
    print("Time:", round(end - start, 6), "sec")


if __name__ == "__main__":
    main()
