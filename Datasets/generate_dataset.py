import random
import pandas as pd

def calculate_calories_needed(age, height, weight, gender, physical_activity):
    if gender == 0:
        # Male
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        # Female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    activity_multipliers = {
        0: 1.2,
        1: 1.375,
        2: 1.55,
        3: 1.725,
        4: 1.9
    }
    
    calories_needed = bmr * activity_multipliers.get(physical_activity, 1.2)
    return calories_needed


# Example usage
age = 30
height = 170
weight = 70
gender = 0  
physical_activity = 2


"""
Mapping

Gender = {
        "male" : 0,
        "female" : 1
}

activity_multipliers = {
        "sedentary": 0,
        "low": 1,
        "moderate": 2,
        "high": 3,
        "very high": 4
    }
"""

# Create an empty list to store the results
results = []

# Set the number of iterations
num_iterations = 5000

for _ in range(num_iterations):
    age = random.randint(18, 60)
    height = random.randint(134, 213)
    weight = random.randint(35, 120)
    gender = random.choice([0, 1])
    physical_activity = random.choice([0, 1, 2, 3, 4])
    
    calories_needed = int(calculate_calories_needed(age, height, weight, gender, physical_activity))
    
    # Store the results as a dictionary
    result = {
        "Age": age,
        "Height(cm)": height,
        "Weight(kg)": weight,
        "Gender": gender,
        "Physical Activity": physical_activity,
        "Calories": calories_needed
    }
    
    results.append(result)

# Create a DataFrame from the results list
df = pd.DataFrame(results)
df.to_csv("calories_needed.csv")