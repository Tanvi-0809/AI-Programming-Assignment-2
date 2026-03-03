"""
Missionaries and Cannibals Problem
State: (M_left, C_left, boat_side)
boat_side: 0 = left, 1 = right
"""

from typing import List, Tuple

State = Tuple[int, int, int]
Action = Tuple[int, int]  # (M_move, C_move)


class MissionariesCannibals:
    def __init__(self, M=3, C=3):
        self.M = M
        self.C = C

    def initial_state(self) -> State:
        return (self.M, self.C, 0)

    def is_goal(self, state: State) -> bool:
        m, c, side = state
        return m == 0 and c == 0 and side == 1

    def valid_state(self, state: State) -> bool:
        m_left, c_left, _ = state
        m_right = self.M - m_left
        c_right = self.C - c_left

        # bounds
        if m_left < 0 or c_left < 0 or m_left > self.M or c_left > self.C:
            return False

        # missionaries not outnumbered
        if m_left > 0 and c_left > m_left:
            return False
        if m_right > 0 and c_right > m_right:
            return False

        return True

    def result(self, state: State, action: Action) -> State:
        m_left, c_left, side = state
        m_move, c_move = action

        if side == 0:  # move left -> right
            return (m_left - m_move, c_left - c_move, 1)
        else:  # move right -> left
            return (m_left + m_move, c_left + c_move, 0)

    def actions(self, state: State) -> List[Action]:
        # boat capacity is 2
        candidates = [(2,0),(0,2),(1,1),(1,0),(0,1)]
        valid_actions = []

        for a in candidates:
            next_state = self.result(state, a)
            if self.valid_state(next_state):
                valid_actions.append(a)

        return valid_actions
