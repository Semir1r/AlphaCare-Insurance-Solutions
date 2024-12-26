import seaborn as sns
import matplotlib.pyplot as plt

def plot_premium_vs_claims_by_vehicle_type(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='VehicleType', y='TotalPremium', data=df, palette='coolwarm', hue='VehicleType')
    plt.title('Insurance Premium vs Total Claims by Vehicle Type')
    plt.xlabel('Vehicle Type')
    plt.ylabel('Insurance Premium')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()