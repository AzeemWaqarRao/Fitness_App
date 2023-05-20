from flask import Flask, request, jsonify
from exercise_recommender import WorkoutPlanner
from meal_recommender import MealPlanner

app = Flask(__name__)

# Define your routes and corresponding handler functions
@app.route('/api/workout-plan', methods=['POST'])
def get_workout_plan():
    # Get the request data
    data = request.json

    # Extract the required parameters from the request data
    age = data.get('age')
    weight = data.get('weight')
    height = data.get('height')
    goal = data.get('goal')
    physical_activity = data.get('physical_activity')
    gender = data.get('gender')

    # Define the workout schedule
    workout_schedule = {
        'Monday': ['chest'],
        'Tuesday': ['upper arms', 'lower arms'],
        'Wednesday': ['back'],
        'Thursday': ['shoulders'],
        'Friday': ['upper legs', 'lower legs'],
        'Saturday': ['cardio']
    }

    # Create the workout planner instance
    workout_planner = WorkoutPlanner(gender, age, weight, height, physical_activity, goal)

    # Generate the workout plan
    workout_plan = workout_planner.suggest_workout_plan(workout_schedule)

    # Return the workout plan as JSON response
    return jsonify(workout_plan)

@app.route('/api/meal-plan', methods=['POST'])
def get_meal_plan():
    # Get the request data
    data = request.json

    # Extract the required parameters from the request data
    age = data.get('age')
    weight = data.get('weight')
    height = data.get('height')
    gender = data.get('gender')
    physical_activity = data.get('physical_activity')
    num_meals = data.get('num_meals')

    # Create the meal planner instance
    meal_planner = MealPlanner(age, height, weight, gender, physical_activity, num_meals)

    # Generate the meal plan
    meal_plan = meal_planner.meal_plans()

    # Return the meal plan as JSON response
    return jsonify(meal_plan)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0')
