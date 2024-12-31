import pandas as pd

def feature_engineering(df):
    """
    Performs feature engineering to create new features relevant to TotalPremium and TotalClaims.

    """
    
    # Step 1: Calculate vehicle age
    current_year = pd.Timestamp.now().year
    df['VehicleAge'] = current_year - df['RegistrationYear']
    
    # Step 2: Create Claims-to-Premium ratio
    df['ClaimsToPremiumRatio'] = df['TotalClaims'] / (df['TotalPremium'] + 1e-5)  # Add small value to avoid division by zero
    
    # Step 3: Create Vehicle Power Index (cubic capacity * kilowatts / cylinders)
    df['VehiclePowerIndex'] = (df['cubiccapacity'] * df['kilowatts']) / (df['Cylinders'] + 1e-5)
    
    # Step 4: Calculate insurance tenure in months (from TransactionMonth to now)
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    df['InsuranceTenureMonths'] = (pd.Timestamp.now() - df['TransactionMonth']).dt.days / 30
    
    # Step 5: Flag high-risk vehicle types (You can adjust based on domain knowledge)
    high_risk_vehicle_types = ['Taxi', 'Truck', 'Bus']  # Example vehicle types
    df['IsHighRiskVehicle'] = df['VehicleType'].apply(lambda x: 1 if x in high_risk_vehicle_types else 0)
    
    # Step 6: Flag high-risk regions based on historical data (e.g., higher claims)
    high_risk_regions = ['RegionA', 'RegionB']  # Replace with actual high-risk regions
    df['IsHighRiskRegion'] = df['Province'].apply(lambda x: 1 if x in high_risk_regions else 0)

    return df