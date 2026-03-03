# AQI Simple Reflex Agent

**Name:** Tanvi Gajula  
**Roll Number:** SE24UCSE025  
**Course:** Artificial Intelligence  

---

## Overview

This module implements a **Simple Reflex Agent** that determines air quality based on environmental sensor input.

The agent reads PM2.5 values from a file and produces an appropriate action using condition-action rules.

---

## Agent Architecture

Sensor → Percept → Condition-Action Rule → Output

### Components:

- **Sensor:** Reads PM2.5 value from `sensor_data.txt`
- **Percept:** Pollution level value
- **Agent Function:** Maps pollution level to AQI category
- **Actuator:** Displays AQI level and recommended action

---

## AQI Categories Implemented

- Good
- Moderate
- Unhealthy for Sensitive Groups
- Unhealthy
- Very Unhealthy
- Hazardous

---

## How It Works

1. Reads PM2.5 value from `sensor_data.txt`.
2. Classifies AQI category.
3. Executes appropriate reflex action.
4. Displays AQI level and advisory message.

---

## Input File

`sensor_data.txt`

Example:
