# main.py
from data_handling import load_data, save_data
from preprocessing import preprocess_data
from model_training import train_model, evaluate_model
from recommendation_engine import recommend_properties
from sklearn.model_selection import train_test_split

def main():
    # Define file path and column names
    file_path = 'property_data.csv'
    target_column = 'Price'
    numerical_features = ['Area', 'Bedrooms', 'Bathrooms', 'Age']
    categorical_features = ['Location', 'Type']

    # Load the dataset
    df = load_data(file_path)

    # Preprocess the data
    X, y = preprocess_data(df, target_column, numerical_features, categorical_features)
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Recommend properties
    recommendations = recommend_properties(df, min_area=1500, max_price=700000, bedrooms=2)
    print("Recommended Properties:")
    print(recommendations)

if _name_ == "_main_":
    main()