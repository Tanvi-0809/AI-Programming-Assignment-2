AI Programming Assignment 2

Name: Tanvi Gajula
Roll Number: SE24UCSE025
Course: Artificial Intelligence

⸻

Introduction

This repository contains the implementation of core Artificial Intelligence concepts as part of Programming Assignment 2. The assignment focuses on Intelligent Agents, Human–Machine differentiation, Simple Reflex Agents, and Uninformed Search strategies. All programs are implemented using Python 3 without any external libraries.

The project is structured into three main problem areas:
	1.	Turing Test and CAPTCHA System
	2.	AQI Simple Reflex Agent
	3.	Uninformed Search using Missionaries and Cannibals Problem

Each section demonstrates practical application of theoretical AI concepts studied in class.

⸻

1️⃣ Turing Test and CAPTCHA System

Turing Test Simulation

Objective

To simulate the Turing Test, where a judge evaluates responses from a human and a machine to determine whether the machine exhibits intelligent behavior similar to a human.

Description

The program generates two types of responses:
	•	Human-like responses that resemble natural conversational language
	•	Machine-like responses that appear structured and robotic

A heuristic judge analyzes the responses using keyword-based scoring. If the suspicion score exceeds a defined threshold, the response is classified as BOT; otherwise, it is classified as HUMAN.

This simulation demonstrates the concept proposed by Alan Turing, where intelligence is judged based on behavior rather than internal processing.

Concepts Demonstrated
	•	Human vs Machine differentiation
	•	Heuristic evaluation
	•	Basic Natural Language imitation
	•	Intelligent Agent behavior

How to Run

Navigate to the Turing_Captcha folder and run:

python3 turingtest.py

⸻

CAPTCHA System

Objective

To design a simple security mechanism that differentiates between human users and automated bots.

Description

The CAPTCHA program randomly generates one of the following challenges:
	•	Math-based challenge (Arithmetic reasoning)
	•	Logic-based question (Common knowledge reasoning)
	•	Text/code verification (Character recognition)

The user must correctly answer the challenge. If the response is correct, access is granted; otherwise, access is blocked.

Architecture

User → Challenge Generation → User Response → Verification → Access Decision

Concepts Demonstrated
	•	Security validation mechanisms
	•	Human cognitive ability testing
	•	Automated bot prevention logic
	•	Simple rule-based verification

How to Run

Navigate to the Turing_Captcha folder and run:

python3 captcha.py

⸻

2️⃣ AQI Simple Reflex Agent

Objective

To implement a Simple Reflex Agent that reads environmental sensor data and performs actions based on predefined condition-action rules.

Description

This agent reads a PM2.5 value from a file named sensor_data.txt. Based on the pollution level, the agent determines the Air Quality Index (AQI) category and outputs an appropriate health advisory.

The agent does not maintain internal memory or history. It simply reacts to the current percept, which makes it a Simple Reflex Agent.

Agent Architecture

Sensor → Percept → Condition-Action Rules → Actuator Output
	•	Sensor: Reads PM2.5 value
	•	Percept: Pollution measurement
	•	Agent Function: Maps pollution level to AQI category
	•	Actuator: Displays advisory message

AQI Categories Implemented
	•	Good
	•	Moderate
	•	Unhealthy for Sensitive Groups
	•	Unhealthy
	•	Very Unhealthy
	•	Hazardous

Concepts Demonstrated
	•	Intelligent Agent Architecture
	•	Simple Reflex Agent model
	•	Condition–Action rules
	•	Real-world AI application

How to Run

Navigate to the AQI_Agent folder and run:

python3 aqi_reflex_agent.py

⸻

3️⃣ Uninformed Search – Missionaries and Cannibals Problem

Objective

To implement Uninformed Search algorithms (Breadth First Search and Depth First Search) to solve a classical state-space problem.

Problem Description

Three missionaries and three cannibals must cross a river using a boat that can carry at most two people.

Constraints
	•	The boat capacity is two persons.
	•	Cannibals must never outnumber missionaries on either bank if missionaries are present.

The goal is to safely move all missionaries and cannibals from the left bank to the right bank.

State Representation

Each state is represented as:

(Missionaries_left, Cannibals_left, Boat_position)

Where:
	•	Missionaries_left = number of missionaries on left bank
	•	Cannibals_left = number of cannibals on left bank
	•	Boat_position = 0 (left bank) or 1 (right bank)

Example: (3, 3, 0) represents the initial state.

Algorithms Implemented

Breadth First Search (BFS)
	•	Explores the search space level by level
	•	Uses a Queue (FIFO structure)
	•	Complete and optimal
	•	Higher memory consumption

Depth First Search (DFS)
	•	Explores deepest nodes first
	•	Uses a Stack (LIFO structure)
	•	Lower memory usage
	•	Not guaranteed to find optimal solution

Performance Metrics Measured
	•	Number of nodes expanded
	•	Maximum frontier size
	•	Execution time

Concepts Demonstrated
	•	State space formulation
	•	Problem representation
	•	Graph search
	•	Uninformed search strategies
	•	Performance comparison between BFS and DFS

How to Run

Navigate to the Search_Algorithms folder and run:

python3 run_compare.py

⸻

Requirements
	•	Python 3
	•	No external libraries required

⸻

Conclusion

This assignment demonstrates fundamental Artificial Intelligence concepts through practical implementation:
	•	Human-machine differentiation using the Turing Test
	•	Security validation through CAPTCHA
	•	Design and implementation of a Simple Reflex Agent
	•	State-space problem solving using Uninformed Search (BFS and DFS)

The project follows modular design principles and clearly reflects theoretical AI concepts through executable Python programs.

⸻
