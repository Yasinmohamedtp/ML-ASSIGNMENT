# model_training.py
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def train_model(X_train, y_train):
    """
    Train a linear regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using test data.
    """
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R-squared (R2 Score): {r2}")

    return rmse, r2