import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importance(model, feature_names, model_name,top_n=20):
    """
    Plots feature importance for tree-based models.
    """
    importance = model.feature_importances_
    sorted_idx = np.argsort(importance)[::-1]
    
    # Display only the top N features for better visibility
    top_idx = sorted_idx[:top_n]
    
    # Create the figure with a larger size for better label visibility
    plt.figure(figsize=(12, 8))
    
    # Set the title for the plot
    plt.title(f"Top {top_n} Feature Importance for {model_name}", fontsize=14)
    
    # Plot the feature importance values
    plt.bar(range(len(top_idx)), importance[top_idx], align="center")
    
    # Set the x-ticks with feature names, rotate for better readability
    plt.xticks(range(len(top_idx)), np.array(feature_names)[top_idx], rotation=90, ha='right', fontsize=10)
    
    # Improve layout to ensure all elements fit
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    

def plot_linear_regression_coefficients(model, feature_names, top_n=20):
    """
    Plots the top N coefficients for Linear Regression.
    
    """
    # Extract coefficients and their corresponding feature names
    coefficients = model.coef_
    sorted_idx = np.argsort(np.abs(coefficients))[::-1][:top_n]  # Select top N features

    # Create the plot
    plt.figure(figsize=(12, 8))  # Increased figure size for better visibility
    plt.title(f"Top {top_n} Linear Regression Coefficients")
    plt.bar(range(len(sorted_idx)), coefficients[sorted_idx], align="center", color='skyblue')
    
    # Adjust the x-axis with selected feature names
    plt.xticks(range(len(sorted_idx)), np.array(feature_names)[sorted_idx], rotation=90, fontsize=10)  # Smaller font size
    
    plt.tight_layout()
    plt.show()