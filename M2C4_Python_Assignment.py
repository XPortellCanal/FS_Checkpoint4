from decimal import Decimal 
#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
work_days= ["monday", "tuesday", "wednesday", "thursday", "friday"]
print(work_days)

weekend_days= ("saturday", "sunday")
print(weekend_days)

item_price=3.3
print(item_price)

car_gear=5
print(car_gear)

flow_rate=Decimal(2.098722)
print(flow_rate)

courses = {
  "monday": ["math", "geography"],
  "tuesday": None,
  "wednesday": ["physics", "chemistry"],
  "thursday": "soil science",
  "friday": None
}
print(courses)

# Exercise 2: Round your float up.
import math
print(math.ceil(item_price))

# Exercise 3: Get the square root of your float.
print(math.sqrt(item_price))

# Exercise 4: Select the first element from your dictionary.
print(courses["monday"])

# Exercise 5: Select the second element from your tuple.
print(weekend_days[1])

# Exercise 6: Add an element to the end of your list.
work_days.extend(["saturday"])
print(work_days)

# Exercise 7: Replace the first element in your list.
work_days[0]="sunday"
print(work_days)

# Exercise 8: Sort your list alphabetically.
work_days.sort()
print(work_days)

# Exercise 9: Use reassignment to add an element to your tuple.
weekend_days+=("monday",)
print(weekend_days)
