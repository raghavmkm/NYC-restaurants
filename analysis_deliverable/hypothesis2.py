import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


#Here we are working on the Kaggle dataset and we are trying to test the following hypothesis:
# Ho - There is no significant difference in the average number of critical violations in Ethnic restaurants
# Ha - There is a significant difference in the average number of critical violations in Ethnic restaurants
# To do this we utilize a One-Sample Proportion Test (One-Sample Z-Test):

def test_hypothesis():
    df = pd.read_csv("../data_deliverable/Clean/violations clean.csv")
    df = df[["CUISINE DESCRIPTION", "CRITICAL FLAG"]]
    ethnic_cuisines = ['Caribbean', 'Afghan', 'Peruvian', 'Ethiopian', 'Filipino', 'Bangladeshi', 'Armenian', 'Egyptian', 'Pakistani']
    ethnic = df[df["CUISINE DESCRIPTION"].isin(ethnic_cuisines)]
    ratio = len(df[df["CRITICAL FLAG"] == "Critical"]) / len(df)
    ethnic_critical = len(ethnic[ethnic["CRITICAL FLAG"] == "Critical"])
    ethnic_total = len(ethnic)
    stat, pval = proportions_ztest(ethnic_critical, ethnic_total, ratio)
    alpha = 0.05  # significance level
    if pval < alpha:
        print("We can reject the Null Hypothesis")
        print(pval)
    else:
        print("We cannot reject the Null Hypothesis")
        print(pval)

def main():
    test_hypothesis()

main()