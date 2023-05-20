import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler



def calories_burnt_predictor():
        
    # Load the dataset
    path = os.path.join('..','Datasets','calories_burnt_dataset.csv')
    df = pd.read_csv(path)

    # Split the dataset into input features (X) and target variable (y)
    X = df[['MET', 'RMR', 'Duration (hours)']]
    y = df['Calories Burnt']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Random Forest Regressor model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    # Save the model as a pickle file
    with open('calories_burnt_model.pkl', 'wb') as file:
        pickle.dump(model, file)


def rmr_predictor():
   
    # Load the dataset
    path = os.path.join("..","Datasets","rmr_dataset.csv")
    df = pd.read_csv(path)

    # Split the dataset into input features (X) and target variable (y)
    X = df[['Gender', 'Age', 'Weight(kg)', 'Height(cm)']]
    y = df['RMR']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define the preprocessor for handling categorical and numerical features
    categorical_cols = ['Gender']
    numerical_cols = ['Age', 'Weight(kg)', 'Height(cm)']

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_cols),
            ('num', StandardScaler(), numerical_cols)
        ])

    # Create a pipeline with the preprocessor and Random Forest Regressor
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    # Save the model and transformer as pickle files
    with open('rmr_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

        
if __name__ == "__main__":
    rmr_predictor()
    calories_burnt_predictor()