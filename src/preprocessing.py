# preprocessing.py
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(df, target_column, numerical_features, categorical_features=None):
    """
    Preprocess the data by handling missing values, encoding categorical features, 
    and standardizing numerical features.
    """
    # Handle missing values (optional strategy: fill or drop)
    df = df.dropna()

    # Encoding categorical variables (if any)
    if categorical_features:
        df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
    
    # Separate features (X) and target (y)
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    # Standardizing numerical features
    scaler = StandardScaler()
    X[numerical_features] = scaler.fit_transform(X[numerical_features])
    
    return X, y
