
AI-Programming-Assignment-2

Artificial Intelligence Programming Assignment 2 implementing Turing Test simulation, CAPTCHA system, AQI Simple Reflex Agent, and Uninformed Search (BFS & DFS) algorithms.


AI Programming Assignment

Name: Tanvi Gajula
Roll Number: SE24UCSE025
Course: Artificial Intelligence


OVERVIEW

This repository contains implementations of fundamental Artificial Intelligence concepts including:

• Turing Test Simulation
• CAPTCHA System
• AQI Simple Reflex Agent
• Missionaries and Cannibals Problem using BFS and DFS

All programs are implemented in Python 3 using only standard libraries without external dependencies.




1️⃣  Turing Test (turingtest.py)

Objective:
To simulate the Turing Test, where a judge attempts to distinguish between a human and a machine based on their responses.

Concept:
The Turing Test evaluates whether a machine can imitate intelligent human behavior convincingly.

Components:

• Machine – Generates robotic-style responses
• Human – Generates natural conversational responses
• Judge – Assigns suspicion score based on keywords

If suspicion score ≥ 40%, the response is classified as BOT, otherwise HUMAN.

How to Run:

cd Turing_Captcha
python3 turingtest.py

⸻

2️⃣ CAPTCHA System (captcha.py)

Objective:
To design a security mechanism that allows human users to pass while blocking automated bots.

CAPTCHA Types Implemented:

Math – Example: What is 12 + 8?
Logic – Example: What comes after Tuesday?
Text – Example: Enter code: ABX9P

Architecture:

User → Challenge Generated → User Response → Verification → Access Granted / Blocked

How to Run:

cd Turing_Captcha
python3 captcha.py

⸻

3️⃣ AQI Simple Reflex Agent (aqi_reflex_agent.py)

Objective:
To implement a Simple Reflex Agent that reads environmental sensor data and produces actions using condition-action rules.

Agent Architecture

Sensor → Percept → Condition-Action Rules → Actuator Output

Working:

• Reads PM2.5 value from sensor_data.txt
• Determines AQI category
• Displays appropriate health advisory

AQI Categories:

Good
Moderate
Unhealthy for Sensitive Groups
Unhealthy
Very Unhealthy
Hazardous

How to Run:

cd AQI_Agent
python3 aqi_reflex_agent.py



4️⃣ Uninformed Search – Missionaries and Cannibals

Objective:
To implement uninformed search strategies (BFS and DFS) to solve a classical state space problem.

Problem Description

Three missionaries and three cannibals must cross a river using a boat of capacity 2.

Constraints:

• The boat can carry at most two people.
• Cannibals must never outnumber missionaries on either bank (if missionaries are present).

State Representation:

State = (Missionaries_left, Cannibals_left, Boat_position)

Example: (3, 3, 0)
Where 0 represents boat on left bank and 1 represents boat on right bank.

Algorithms Implemented:
	1.	Breadth First Search (BFS)
• Explores level by level
• Uses Queue (FIFO)
• Complete and optimal
• Higher memory usage
	2.	Depth First Search (DFS)
• Explores deepest node first
• Uses Stack (LIFO)
• Lower memory usage
• Not always optimal

Performance Metrics Measured:

• Nodes Expanded
• Maximum Frontier Size
• Execution Time

How to Run:

cd Search_Algorithms
python3 run_compare.py



Performance Comparison:

BFS:
Time Complexity: O(b^d)
Space Complexity: O(b^d)

DFS:
Time Complexity: O(b^d)
Space Complexity: O(d)

Where
b = branching factor
d = depth of solution



Requirements:

Python 3
No external libraries required


Conclusion:

This assignment demonstrates:

• Human vs Machine differentiation using the Turing Test
• Security validation mechanism using CAPTCHA
• Simple Reflex Agent design using environmental sensors
• State space formulation and problem solving using Uninformed Search
• Practical implementation of BFS and DFS algorithms

All implementations follow modular design and standard AI problem-solving principles.
