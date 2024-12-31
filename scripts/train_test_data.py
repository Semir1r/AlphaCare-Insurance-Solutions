from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def convert_datetime_to_numeric(df):
    """
    Converts datetime columns to numeric values.
    Extract useful features from datetime columns.
    """
    # Identify datetime columns
    datetime_columns = df.select_dtypes(include=['datetime', 'datetime64']).columns
    
    for col in datetime_columns:
        # Convert datetime to numeric by extracting useful parts or converting to timestamp
        df[col + '_year'] = df[col].dt.year
        df[col + '_month'] = df[col].dt.month
        df[col + '_day'] = df[col].dt.day
        df[col + '_weekday'] = df[col].dt.weekday
        
        # Optionally, you can remove the original datetime column if not needed
        df.drop(columns=[col], inplace=True)
    
    return df


def clean_data_for_modeling(df):
    """
    Clean the dataset by replacing or removing non-numeric values that may prevent the model from training.
    """
    # Replace 'Not specified' and other non-numeric entries with NaN
    df.replace('Not specified', np.nan, inplace=True)
    df.replace('Unknown', np.nan, inplace=True)

    
    # Fill missing values with the median for numerical columns
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # For categorical columns, you can use mode or drop the rows
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    

    for col in df.columns:
        if df[col].dtype == 'object':  # Check if the column is object type (usually indicates strings)
            df[col] = df[col].str.replace(',', '', regex=False)  # Remove commas from numbers
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, setting invalid parsing as NaN
    
    return df


def train_test_split_data(df, target_column, test_size=0.3, random_state=42):
    """
    Splits the data into training and testing sets for modeling.
    
    """
    
    # Step 1: Separate features (X) and target (y)
    X = df.drop(columns=[target_column])  # Features (all columns except target)
    y = df[target_column]  # Target variable
    
    # Step 2: Perform train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test