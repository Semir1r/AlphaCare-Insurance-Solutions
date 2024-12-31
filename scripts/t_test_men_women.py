import scipy.stats as stats

def t_test_men_women(df_male, df_female, kpi_column):
    # Perform t-test
    t_stat, p_value = stats.ttest_ind(df_male[kpi_column].dropna(), df_female[kpi_column].dropna(), equal_var=False)
    return t_stat, p_value
