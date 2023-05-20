import pandas as pd
import pickle
import os

def predict_rmr(Gender, age, weight, height):
    # Load the saved model and transformer
    path = os.path.join('Exercise_Models','rmr_model.pkl')
    with open(path, 'rb') as model_file:
        model = pickle.load(model_file)
        

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({'Gender': [Gender], 'Age': [age], 'Weight(kg)': [weight], 'Height(cm)': [height]})

    # Preprocess the input data using the saved transformer
    # preprocessed_data = transformer.transform(input_data)

    # Predict the RMR value using the trained model
    rmr_prediction = model.predict(input_data)

    return int(rmr_prediction[0])


def predict_calories_burnt(met, rmr, duration):
    # Load the saved model
    path = os.path.join("Exercise_Models","calories_burnt_model.pkl")
    with open(path, 'rb') as model_file:
        model = pickle.load(model_file)

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({'MET': [met], 'RMR': [rmr], 'Duration (hours)': [duration]})

    # Predict the calories burnt using the trained model
    calories_burnt = model.predict(input_data)

    return int(calories_burnt[0])
