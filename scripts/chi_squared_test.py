import pandas as pd
import scipy.stats as stats
from scipy.stats import chi2_contingency, ttest_ind

def chi_squared_test(group_a, group_b, feature_column):
    """
    Perform a chi-squared test to check if there is a significant difference
    between two groups for a categorical feature.
    """
    combined = pd.concat([group_a, group_b])

    # Create the contingency table
    contingency_table = pd.crosstab(combined[feature_column], combined.index)

    # Perform the chi-squared test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p