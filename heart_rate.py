#Heart rate calculator
"""
When you physically exercise to strengthen your heart, 
you should maintain your heart rate within a range for at least 20minutes. 
To find that range, subtract your age from 220. 
This difference is your maximum heart rate per minute. 
Your heart simply will not beat faster than this maximum 220 - age).
When exercising to strengthen your heart, 
you should keep your heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("What is your age? "))

heart_range = 220 - age

min_heart_rate = heart_range * 65 / 100

max_heart_rate = heart_range * 85 / 100

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {round(min_heart_rate)} and {round(max_heart_rate)} beats per minute.")

