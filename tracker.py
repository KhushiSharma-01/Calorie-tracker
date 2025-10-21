# Name : Khushi Sharma
# Date : 11/10/25
# Project Title : Daily Calorie Tracker

# welcome message and program introduction
print("Welcome to the Daily Calorie Tracker!")
print("This program helps you track your daily calorie intake .")
print("You can enter the food items you consume along with their calorie values.")
print("At the end of the day, you'll get a summary of your total calorie intake.")

# List to store meal names and calories and take input from the user
meals = []
calories = []
num_meals = int(input("Enter the number of meals you had today: "))
 # loop to collect meal data 
for i in range(num_meals):
     meal_name = input(f"Enter the name of meal {i+1}: ")
     calorie_value = int(input(f"Enter the calorie value for {meal_name}: "))
     meals.append(meal_name)
     calories.append(calorie_value)

     print("Your meals and calories today :")
     for i in range(len(meals)):
        print(f"{meals[i]}: {calories[i]} calories")
# Calculate total calories
total_calories = sum(calories) 
avg_calories = total_calories / num_meals if num_meals > 0 else 0
print(f"Average calorie intake per meal: {avg_calories:.2f} calories")
print(f"Total calorie intake for the day: {total_calories} calories")

daily_limit = float(input("Enter your daily calorie limit: "))
if total_calories > daily_limit:
        print("You have exceeded your daily calorie limit. Try to eat healthier tomorrow!")
elif total_calories == daily_limit:
        print("You have met your daily calorie limit exactly. Good job!")
else:
        print("Great job! You are within your daily calorie limit.")
if total_calories > daily_limit :
     print("Warning: You have exceeded your daily calorie limit!")
else:
     print("You are within your daily calorie limit.")
print("Your Daily calorie summary:")
print(f"{'mael_name':<15}"
{'calories':>8.2})
print("-"*25)
for i in range(len(meals)):
    print(f"{meals[i]:<15}{calories[i]:>8}")
print("-"*25)
print(f"{'Total:'<15}
{'total_calories:'> 8}")

 
