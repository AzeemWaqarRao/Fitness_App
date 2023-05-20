import pandas as pd
import pickle

def predict_calories(age, height, weight, gender, physical_activity):
    # Create a DataFrame with the input parameters
    gender_mapping = {"male": 0, "female": 1}
    mapped_gender = gender_mapping.get(gender)

    physical_activity_mapping = {
        "sedentary": 0,
        "low": 1,
        "moderate": 2,
        "high": 3,
        "very high": 4
    }
    mapped_physical_activity = physical_activity_mapping.get(physical_activity)

    test_data = pd.DataFrame({
        'Age': [age],
        'Height(cm)': [height],
        'Weight(kg)': [weight],
        'Gender': [mapped_gender],
        'Physical Activity': [mapped_physical_activity]
    })

    # Load the scaler object from the pickle file
    scaler_filename = 'Meal_Models/scaler.pickle'
    with open(scaler_filename, 'rb') as f:
        scaler = pickle.load(f)

    # Perform scaling on the test data
    test_data_scaled = scaler.transform(test_data)

    # Load the trained model from the pickle file
    model_filename = 'Meal_Models/model.pickle'
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)

    # Make predictions on the scaled test data
    predictions = int(model.predict(test_data_scaled))

    return predictions

if __name__ == "__main__":
    # Example usage
    age = 30
    height = 180
    weight = 75
    gender = 'male'
    physical_activity = 2

    # Call the function to make predictions
    results = predict_calories(age, height, weight, gender, physical_activity)

    # Print the predictions
    print(results)
