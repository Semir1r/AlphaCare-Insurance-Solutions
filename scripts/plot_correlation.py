import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(df, columns):
    plt.figure(figsize=(10, 8))
    corr_matrix = df[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, square=True)
    plt.title('Correlation Matrix')
    plt.show()