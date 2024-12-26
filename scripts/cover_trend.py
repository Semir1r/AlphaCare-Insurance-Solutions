import matplotlib.pyplot as plt
import seaborn as sns

def plot_cover_type_trends(df, geo_col, cover_col):
    plt.figure(figsize=(12, 6))
    sns.countplot(x=geo_col, hue=cover_col, data=df, palette='Set2')
    plt.title(f'Comparison of {cover_col} across {geo_col}')
    plt.xticks(rotation=45)
    plt.xlabel(geo_col)
    plt.ylabel('Count')
    plt.legend(title=cover_col)
    plt.grid(True)
    plt.show()