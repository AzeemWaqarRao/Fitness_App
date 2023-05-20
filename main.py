from exercise_recommender import WorkoutPlanner
from meal_recommender import MealPlanner

age = 22                        # in years
weight = 65                     # in KGs
height = 165                    # in CMs
goal = 'weight_gain'            # 'weight_gain' or 'weight_loss'
physical_activity = 'high'      #"sedentary" , "low" ,"moderate" , "high" , "very high"
gender = 'male'                 # 'male' or 'female'
num_meals = 5                   # 3 to 6
workout_schedule = {
        'Monday': ['chest'],
        'Tuesday': ['upper arms', 'lower arms'],
        'Wednesday': ['back'],
        'Thursday': ['shoulders'],
        'Friday': ['upper legs', 'lower legs'],
        'Saturday': ['cardio']
    }

    
workout_planner = WorkoutPlanner(gender, age, weight, height, physical_activity, goal)
meal_planner = MealPlanner(age, height, weight, gender, physical_activity, num_meals)

print('####### WORKOUT PLAN #######')
print(workout_planner.suggest_workout_plan(workout_schedule))

print('####### MEAL PLAN #######')
print(meal_planner.meal_plans())