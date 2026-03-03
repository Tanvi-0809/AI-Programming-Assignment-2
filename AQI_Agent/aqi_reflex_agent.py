"""
AQI Simple Reflex Agent
 Tanvi Gajula
 SE24UCSE025
Course: Artificial Intelligence

Description:
Reads environmental data from a file (sensor input),
calculates AQI category, and outputs action based on rules.
"""

def calculate_aqi(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    elif pm25 <= 150:
        return "Unhealthy for Sensitive Groups"
    elif pm25 <= 200:
        return "Unhealthy"
    elif pm25 <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


def reflex_action(category):
    if category == "Good":
        return "Air quality is good. Normal outdoor activity."
    elif category == "Moderate":
        return "Acceptable. Sensitive individuals should be cautious."
    elif category == "Unhealthy for Sensitive Groups":
        return "Sensitive groups should limit outdoor activity."
    elif category == "Unhealthy":
        return "Avoid prolonged outdoor exertion."
    elif category == "Very Unhealthy":
        return "Stay indoors if possible."
    else:
        return "Health alert! Avoid going outside."


def main():
    print("=== AQI SIMPLE REFLEX AGENT ===")

    # Reading sensor data from file
    try:
        with open("sensor_data.txt", "r") as file:
            pm25 = int(file.read().strip())
    except:
        print("Error: sensor_data.txt not found.")
        return

    category = calculate_aqi(pm25)
    action = reflex_action(category)

    print("PM2.5 Value:", pm25)
    print("AQI Category:", category)
    print("Agent Action:", action)


if __name__ == "__main__":
    main()
