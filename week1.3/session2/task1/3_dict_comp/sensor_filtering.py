# Week 1.3, Session 2: Home Sensor Filtering

home_sensors = {"Living Room Thermostat": 85, "Front Door Lock": 15, "Kitchen Smoke Detector": 90, "Basement Flood Sensor": 8}

# dictionary comprehension to filter all sensors with battery level less than 20
# Expected Output: {'Front Door Lock': 15, 'Basement Flood Sensor': 8}

dying_home_sensors = {key:home_sensors[key] for key in home_sensors if home_sensors[key]<20}

# print the new dictionary with battery less than 20 to verify
print(dying_home_sensors)
