# Q3 — Uninformed Search Algorithms (Missionaries & Cannibals)

**Name:** Tanvi Gajula  
**Roll No:** SE24UCSE025  

## Problem
3 Missionaries and 3 Cannibals must cross a river using a boat of capacity 2.  
Rule: Cannibals must never outnumber missionaries on either bank (if missionaries are present).

## State Representation
State = (M_left, C_left, boat_side)  
boat_side = 0 (left bank), 1 (right bank)

## Algorithms Implemented
- Breadth First Search (BFS) — uses FIFO queue
- Depth First Search (DFS) — uses LIFO stack

## Performance Metrics
- Nodes expanded
- Maximum frontier size
- Execution time

## Run
```bash
python3 run_compare.py
