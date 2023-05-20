import pandas as pd
import os
import json
from Exercise_Models.utils import predict_calories_burnt, predict_rmr
from Meal_Models.calories_predictor import predict_calories


class WorkoutPlanner:
    def __init__(self, gender, age, weight, height, physical_activity, goal):
        
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.dataset_path = os.path.join('Datasets','fitness_exercises.csv')
        self.exercise_df = pd.read_csv(self.dataset_path)
        self.calories_to_consume = predict_calories(age, height, weight, gender, physical_activity)
        self.calories_to_burn = self.calculate_calories_to_burn(self.calories_to_consume, goal)

    def map_intensity_to_met(self):
        met_mapping = {'normal': 3.5, 'intermediate': 5}
        self.exercise_df['MET'] = self.exercise_df['intensity'].map(met_mapping)

    def add_calories_burnt_column(self):
        self.map_intensity_to_met()

        RMR = predict_rmr(self.gender, self.age, self.weight, self.height)

        self.exercise_df['Calories Burnt'] = self.exercise_df.apply(lambda row: predict_calories_burnt(row['MET'], RMR, round(5/60, 4)), axis=1)
        self.exercise_df.to_csv(self.dataset_path, index=False)

    def suggest_workout_plan(self, workout_schedule):
        self.add_calories_burnt_column()

        workout_plan = {}
        for day, body_parts in workout_schedule.items():
            selected_exercises = []
            total_calories_burnt = 0

            for body_part in body_parts:
                exercises = self.exercise_df[self.exercise_df['bodyPart'] == body_part]

                while total_calories_burnt < self.calories_to_burn:
                    exercise = exercises.sample(n=1)

                    if total_calories_burnt + exercise['Calories Burnt'].values[0] <= self.calories_to_burn:
                        selected_exercises.append(exercise['name'].values[0])
                        total_calories_burnt += exercise['Calories Burnt'].values[0]
                    else:
                        break

            workout_plan[day] = selected_exercises

        return workout_plan

    def calculate_calories_to_burn(self, calorie_intake, goal):
        if goal == "weight_gain":
            calorie_surplus = calorie_intake * 0.1
        elif goal == "weight_loss":
            calorie_surplus = -1 * calorie_intake * 0.2
        else:
            raise ValueError("Invalid goal. Supported goals: 'weight_gain', 'weight_loss'")

        calories_to_burn = calorie_intake - calorie_surplus
        return calories_to_burn


if __name__ == "__main__":
        
    # Define the workout schedule
    workout_schedule = {
        'Monday': ['chest'],
        'Tuesday': ['upper arms', 'lower arms'],
        'Wednesday': ['back'],
        'Thursday': ['shoulders'],
        'Friday': ['upper legs', 'lower legs'],
        'Saturday': ['cardio']
    }
    age = 22
    weight = 65
    height = 160
    gender = 'male'
    goal = "weight_gain"
    physical_activity = 'high'


    # Create an instance of WorkoutPlanner
    workout_planner = WorkoutPlanner(gender, age, weight, height, physical_activity, goal)

    # Example usage

    workout_plan = workout_planner.suggest_workout_plan(workout_schedule)

    # Print the workout plan
    print(workout_plan)
