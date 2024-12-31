import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_categorical_data(df):
    """
    Encodes categorical data using Label Encoding for binary categories
    and One-Hot Encoding for non-binary categories.
    """
    # Columns to apply Label Encoding (for binary and ordinal categories)
    label_encode_columns = ['NewVehicle', 'WrittenOff', 'Rebuilt', 'Converted', 'CrossBorder', 'AlarmImmobiliser', 
                            'TrackingDevice', 'MaritalStatus', 'Gender', 'VehicleType']  # Added 'VehicleType'
    
    # Apply Label Encoding to binary/ordinal columns
    for col in label_encode_columns:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str).fillna('Unknown'))  # Handle missing values as 'Unknown'
    
    # Columns to apply One-Hot Encoding (for nominal categories with multiple values)
    one_hot_encode_columns = ['Citizenship', 'LegalType', 'Title', 'Language', 'Bank', 'AccountType', 'Country', 
                              'MainCrestaZone', 'SubCrestaZone', 'ItemType', 'make', 'Model', 'bodytype', 'TermFrequency', 
                              'ExcessSelected', 'CoverCategory', 'CoverType', 'CoverGroup', 'Section', 'Product', 
                              'StatutoryClass', 'StatutoryRiskType', 'Province']  # Added 'Province' earlier
    
    # Apply One-Hot Encoding to nominal columns
    df = pd.get_dummies(df, columns=one_hot_encode_columns, drop_first=True)
    
    return df