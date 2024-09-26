# ML-ASSIGNMENT
his project predicts property prices using machine learning models based on various features like location, area, number of bedrooms, bathrooms, and property age. The project is modularized to improve scalability and maintainability, separating data handling, preprocessing, model training, and recommendation logic into different Python files.

Modules Overview
Data Handling Module (data_handling.py):

Loads the dataset from a CSV file and provides a function to save processed data.
Functions: load_data(), save_data()
Preprocessing Module (preprocessing.py):

Preprocesses the data by handling missing values, encoding categorical features, and scaling numerical data.
Functions: preprocess_data()
Model Training Module (model_training.py):

Trains a machine learning model (currently using Linear Regression) and evaluates it using test data.
Functions: train_model(), evaluate_model()
Recommendation Engine (recommendation_engine.py):

Recommends properties based on user-defined criteria such as minimum area, maximum price, and number of bedrooms.
Functions: recommend_properties()
Main Script (main.py):

The main script that ties together all the modules. It loads the data, preprocesses it, trains the model, evaluates it, and then generates property recommendations.
Dataset
The dataset should be in CSV format and contain the following columns:

Location: The city or area where the property is located.
Area (sq.ft): The size of the property in square feet.
Bedrooms: Number of bedrooms in the property.
Bathrooms: Number of bathrooms in the property.
Age (years): The age of the property in years.
Type: Type of property (e.g., Apartment, Villa).
Price: The price of the property (target variable).


Dataset
The dataset should be in CSV format and contain the following columns:

Location: The city or area where the property is located.
Area (sq.ft): The size of the property in square feet.
Bedrooms: Number of bedrooms in the property.
Bathrooms: Number of bathrooms in the property.
Age (years): The age of the property in years.
Type: Type of property (e.g., Apartment, Villa).
Price: The price of the property (target variable).