import pandas as pd
import numpy as np

#Here we are working on the Kaggle dataset and we are trying to test the following hypothesis:
# Ho - There is no significant difference in the ratings of restaurants in the highest price category
# Ha - There is a significant difference in the ratings of restaurants in the highest price category

def test_hypothesis():
    df = pd.read_csv("../data_deliverable/Clean/Cleaned Restaurant data.csv")
    expensive = df[df["Price Category"] == 4.0]
    expensive = expensive[["Rating", "Price Category"]]
    total_mean = np.mean(df[["Rating"]])
    expensive_mean = np.mean(expensive[["Rating"]])
    n = np.shape(expensive)[0]
    std_dev = np.sqrt(np.var(df[["Rating"]]))
    z = (expensive_mean - total_mean) / (std_dev / np.sqrt(n))
    z = z.iloc[0]
    if(z > 1.96 or z < -1.96):
        print("We can reject the Null Hypothesis")
    else:
        print("We cannot reject the Null Hypothesis")


def main():
    test_hypothesis()

main()