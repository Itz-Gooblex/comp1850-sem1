"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
change_time = 0

while systime < maxtime:
    change_time += 1
    systime += 1

    if states[state] == change_time:
        match state:
            case "red":
                state = "red_amber"
            case "red_amber":
                state = "green"
            case "green":
                state = "amber"
            case "amber":
                state = "red"
        
        change_time = 0

    print(f"Time {systime:03} State {state}")
# At the end of each step you should output the time and state using the statement on line 14