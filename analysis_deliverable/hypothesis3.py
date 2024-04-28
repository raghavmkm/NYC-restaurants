import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


#Here the statistic we are using to test our hypothesis is the Chi square test of independence. We want to check if there is an association
# between the Borough and the number of critical flags. Our thesis is that since different borough have different levels of affluence, there might
# be a relationship between the boroughs and the number of ciritcal flags. The Null being there is no strong relationship and the borough and 
#critical violations are independent

def test_hypothesis():
    df = pd.read_csv("../data_deliverable/Clean/violations clean.csv")
    df = df[["BORO", "CRITICAL FLAG"]].dropna()
    manhattan = df[df["BORO"] == "Manhattan"]
    manhattan_crit = len(manhattan[manhattan["CRITICAL FLAG"] == "Critical"])
    manhattan_non_crit = len(manhattan[manhattan["CRITICAL FLAG"] == "Not Critical"])
    brooklyn = df[df["BORO"] == "Brooklyn"]
    brooklyn_crit = len(brooklyn[brooklyn["CRITICAL FLAG"] == "Critical"])
    brooklyn_non_crit = len(brooklyn[brooklyn["CRITICAL FLAG"] == "Not Critical"])
    bronx = df[df["BORO"] == "Bronx"]
    bronx_crit = len(bronx[bronx["CRITICAL FLAG"] == "Critical"])
    bronx_non_crit = len(bronx[bronx["CRITICAL FLAG"] == "Not Critical"])
    queens = df[df["BORO"] == "Queens"]
    queens_crit = len(queens[queens["CRITICAL FLAG"] == "Critical"])
    queens_non_crit = len(queens[queens["CRITICAL FLAG"] == "Not Critical"])
    staten = df[df["BORO"] == "Staten Island"]
    staten_crit = len(staten[staten["CRITICAL FLAG"] == "Critical"])
    staten_non_crit = len(staten[staten["CRITICAL FLAG"] == "Not Critical"])
    observed = np.array([[manhattan_crit, manhattan_non_crit],
                     [brooklyn_crit, brooklyn_non_crit],
                     [bronx_crit, bronx_non_crit],
                     [queens_crit, queens_non_crit],
                     [staten_crit, staten_non_crit]]) 
    chi2_stat, p_val, dof, expected = chi2_contingency(observed)
    alpha = 0.05  
    print("Chi-square statistic:", chi2_stat)
    print("P-value:", p_val)
    if p_val < alpha:
        print("We can reject the Null Hypothesis")
    else:
        print("We cannot reject the Null Hypothesis")


def main():
    test_hypothesis()

main()