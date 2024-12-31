import scipy.stats as stats

def anova_test_for_postalcode_margin(df, kpi_column, group_column):
    # Get unique postal codes
    postal_codes = df[group_column].unique()
    print(postal_codes)
    # Prepare data for ANOVA: collect 'Margin' for each postal code
    postal_groups = [df[df[group_column] == postal_code][kpi_column].dropna() for postal_code in postal_codes]

    # Perform ANOVA
    f_stat, p_value = stats.f_oneway(*postal_groups)

    return f_stat, p_value