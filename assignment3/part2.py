# Ask the user for the current time (in hours)
current_time = int(input("Enter the current time (in hours): "))

# Ask the user for the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm goes off
alarm_time = (current_time + hours_to_wait) % 24

# Output the alarm time
print("The alarm will go off at", alarm_time, "hours on a 24-hour clock.")