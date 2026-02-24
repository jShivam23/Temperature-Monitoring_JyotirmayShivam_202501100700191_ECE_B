import random
import time

# Accept max and min limit temperature
min_temp = int(input("Enter minimum temperature: "))
max_temp = int(input("Enter maximum temperature: "))

# Generate random values at every 2 second interval
while True:
    temp = random.randint(0, 100)
    print(f"\nCurrent Temperature: {temp}")

    # Compare with the limits and display messages
    if temp > max_temp:
        print("Alert: Temperature is too high")
    elif temp < min_temp:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")

    time.sleep(2)