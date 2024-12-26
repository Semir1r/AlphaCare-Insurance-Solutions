import pandas as pd
import matplotlib.pyplot as plt

def handle_missing_values(df):
    # Fill missing values for categorical columns with 'Unknown' or mode
    categorical_columns = ['Bank', 'AccountType', 'MaritalStatus', 'Gender', 'VehicleType', 'make', 'Model',
                           'NewVehicle', 'WrittenOff', 'Rebuilt', 'Converted', 'CrossBorder', 'AlarmImmobiliser',
                           'TrackingDevice'] 
    for col in categorical_columns:
        df[col] = df[col].fillna('Unknown')

    # Fill missing values for columns where the mode is appropriate
    mode_columns = ['mmcode', 'bodytype', 'CapitalOutstanding']
    for col in mode_columns:
        mode_value = df[col].mode()[0]  # Get the most frequent value
        df[col] = df[col].fillna(mode_value)

    # Handle date columns separately - Convert to datetime format first
    if 'VehicleIntroDate' in df.columns:
        df['VehicleIntroDate'] = pd.to_datetime(df['VehicleIntroDate'], errors='coerce')  # Convert to datetime
        df['VehicleIntroDate'] = df['VehicleIntroDate'].fillna(df['VehicleIntroDate'].median())  # Fill missing dates

    # Fill missing values for numerical columns with the median
    numerical_columns = ['Cylinders', 'cubiccapacity', 'kilowatts', 'NumberOfDoors', 'CustomValueEstimate']
    
    for col in numerical_columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
    
    # Special handling for 'NumberOfVehiclesInFleet'
    if 'NumberOfVehiclesInFleet' in df.columns:
        # Fill with a default value, e.g., '1' or '0' if missing
        df['NumberOfVehiclesInFleet'] = df['NumberOfVehiclesInFleet'].fillna(1)  # Assuming most are individual vehicles
    
    return df