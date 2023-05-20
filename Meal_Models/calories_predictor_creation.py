import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import os


def calories_predictor_creation():
    # Load the dataset
    dataset_path = os.path.join('..','Datasets','calories_needed.csv')
    df = pd.read_csv(dataset_path)  # Replace 'your_dataset.csv' with the actual filename

    # Separate the features (input) and target (output) columns
    X = df.drop(['Calories', 'Unnamed: 0'], axis=1)
    y = df['Calories']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and fit the StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Save the scaler object to a pickle file
    with open('scaler.pickle', 'wb') as f:
        pickle.dump(scaler, f)

    # Initialize and train the Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Perform scaling on the test data
    X_test_scaled = scaler.transform(X_test)

    # Make predictions on the test data
    y_pred = model.predict(X_test_scaled)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Save the trained model to a pickle file
    with open('model.pickle', 'wb') as f:
        pickle.dump(model, f)

    return mse, r2


if __name__ == "__main__":
    mse, r2 = calories_predictor_creation()
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

