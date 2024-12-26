import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatter(cleaned_data):
    
    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        data=cleaned_data,
        x='TotalPremium',
        y='TotalClaims',
        hue='PostalCode',  # Ensure this matches the correct column name
        palette='viridis',
        alpha=0.7
    )
    plt.title('TotalPremium vs TotalClaims (Grouped by PostalCode)')
    plt.xlabel('TotalPremium')
    plt.ylabel('TotalClaims')
    plt.legend(title='PostalCode', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.show()
