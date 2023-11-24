import re

input_str = input()

# Define the regular expression to match each food item's information
pattern = (
    r"(#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"
)

matches = re.finditer(pattern, input_str)

total_calories = 0
food_items = []

# Iterate through the matches and collect food items' information
for match in matches:
    item_name = match.group("item")
    expiration_date = match.group("date")
    calories = int(match.group("calories"))

    total_calories += calories
    food_items.append(
        f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}"
    )

# Calculate the number of days the astronaut can last with the available food
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

# Print information about each food item
for food in food_items:
    print(food)
