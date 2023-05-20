import pandas as pd
from random import randint
from Meal_Models.calories_predictor import predict_calories
import os

class MealPlanner:

    def __init__(self, age, height, weight, gender, physical_activity, num_meals):
        # Load the dataset
        self.dataset_path = os.path.join('Datasets','food items.csv')
        self.dataset = pd.read_csv(self.dataset_path)
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.physical_activity = physical_activity
        self.num_meals = num_meals
        self.tdee = predict_calories(self.age, self.height, self.weight, self.gender, self.physical_activity)

        # Create lists of food items for each category
        self.meat_items = self.dataset[self.dataset['Category'] == 'meat']['food items'].tolist()
        self.dairy_items = self.dataset[self.dataset['Category'] == 'dairy']['food items'].tolist()
        self.snacks_items = self.dataset[self.dataset['Category'] == 'snacks']['food items'].tolist()
        self.sides_items = self.dataset[self.dataset['Category'] == 'sides']['food items'].tolist()
        self.fruit_items = self.dataset[self.dataset['Category'] == 'fruits']['food items'].tolist()
        self.drinks_items = self.dataset[self.dataset['Category'] == 'drinks']['food items'].tolist()
        self.soups_items = self.dataset[self.dataset['Category'] == 'soups']['food items'].tolist()
        self.salads_items = self.dataset[self.dataset['Category'] == 'salad']['food items'].tolist()
        self.extras_items = self.dataset[self.dataset['Category'] == 'extras']['food items'].tolist()

    def bfcalc(self):
        # Generate breakfast plan
        breakfast = [self.dairy_items[randint(0, len(self.dairy_items) - 1)], self.fruit_items[randint(0, len(self.fruit_items) - 1)]]

        if self.tdee >= 2200:
            breakfast.append(self.drinks_items[randint(0, len(self.drinks_items) - 1)])

        return breakfast

    def s1calc(self):
        # Generate snack 1 plan
        snack1 = []
        if self.tdee >= 1800:
            snack1.append(self.snacks_items[randint(0, len(self.snacks_items) - 1)])

        return snack1

    def lcalc(self):
        # Generate lunch plan
        lunch = [self.meat_items[randint(0, len(self.meat_items) - 1)], self.sides_items[randint(0, len(self.sides_items) - 1)],
                 self.drinks_items[randint(0, len(self.drinks_items) - 1)], self.salads_items[randint(0, len(self.salads_items) - 1)]]

        if self.tdee >= 1500:
            lunch.append(self.fruit_items[randint(0, len(self.fruit_items) - 1)])

        if self.tdee >= 1800:
            lunch.append(self.snacks_items[randint(0, len(self.snacks_items) - 1)])

        return lunch

    def s2calc(self):
        # Generate snack 2 plan
        snack2 = [self.snacks_items[randint(0, len(self.snacks_items) - 1)], self.extras_items[randint(0, len(self.extras_items) - 1)]]
        return snack2

    def dcalc(self):
        # Generate dinner plan
        dinner = [self.meat_items[randint(0, len(self.meat_items) - 1)], self.drinks_items[randint(0, len(self.drinks_items) - 1)],
                  self.soups_items[randint(0, len(self.soups_items) - 1)]]

        if self.tdee >= 1500:
            dinner.append(self.dairy_items[randint(0, len(self.dairy_items) - 1)])

        if self.tdee >= 2200:
            dinner.append(self.fruit_items[randint(0, len(self.fruit_items) - 1)])
            dinner.append(self.extras_items[randint(0, len(self.extras_items) - 1)])

        return dinner

    def s3calc(self):
        # Generate snack 3 plan
        snack3 = [self.snacks_items[randint(0, len(self.snacks_items) - 1)]]
        return snack3

    def meal_plans(self):
        # Generate meal plans based on the TDEE and number of meals
        plans = {}
        functions = {'Breakfast': self.bfcalc, 'Lunch': self.lcalc, 'Dinner': self.dcalc, 'Snack 1': self.s1calc,
                     'Snack 2': self.s2calc, 'Snack 3': self.s3calc}

        for i in range(self.num_meals):
            meal_name = list(functions.keys())[i]
            meal_plan = functions[meal_name]()
            plans[meal_name] = meal_plan

        return plans



if __name__ == "__main__":
		
    """
    activity_multipliers = {
        "sedentary": 0,
        "low": 1,
        "moderate": 2,
        "high": 3,
        "very high": 4
    }
    """
	# Example usage
    meal_planner = MealPlanner(age=22, height=170, weight=65, gender='male', physical_activity='high', num_meals=5)
    meal_dict = meal_planner.meal_plans()
    print(meal_dict)



