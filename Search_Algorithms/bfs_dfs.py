"""
BFS and DFS for Missionaries & Cannibals
Includes performance metrics: nodes expanded, max frontier size
"""

from collections import deque


def bfs(problem):
    start = problem.initial_state()
    frontier = deque([(start, [])])  # queue: (state, path)
    explored = set()

    nodes_expanded = 0
    max_frontier = 1

    while frontier:
        max_frontier = max(max_frontier, len(frontier))
        state, path = frontier.popleft()

        if problem.is_goal(state):
            return path, nodes_expanded, max_frontier

        if state in explored:
            continue
        explored.add(state)

        nodes_expanded += 1
        for action in problem.actions(state):
            next_state = problem.result(state, action)
            if next_state not in explored:
                frontier.append((next_state, path + [action]))

    return None, nodes_expanded, max_frontier


def dfs(problem):
    start = problem.initial_state()
    frontier = [(start, [])]  # stack
    explored = set()

    nodes_expanded = 0
    max_frontier = 1

    while frontier:
        max_frontier = max(max_frontier, len(frontier))
        state, path = frontier.pop()

        if problem.is_goal(state):
            return path, nodes_expanded, max_frontier

        if state in explored:
            continue
        explored.add(state)

        nodes_expanded += 1
        for action in problem.actions(state):
            next_state = problem.result(state, action)
            if next_state not in explored:
                frontier.append((next_state, path + [action]))

    return None, nodes_expanded, max_frontier
