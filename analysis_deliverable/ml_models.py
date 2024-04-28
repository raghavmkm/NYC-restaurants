import pandas as pd
import sklearn as skl
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np


def get_model_1_data():
    # Predict health violation based on neighbourhood affluence and cuisine type

    violations_df = pd.read_excel("../data_deliverable/Clean/violations clean.xlsx")
    # Make Critical a binary value as it is the target
    violations_df["CRITICAL"] = violations_df["CRITICAL FLAG"].map({'Critical': 1, 'Not Critical': 0})

    # get median income data and rename a column
    income_df = pd.read_csv("../data_deliverable/Clean/Median Incomes 2021 Clean.csv") 
    income_df.rename(columns={"Median Household Income 2021": "MEDIAN_INCOME"}, inplace=True)

    # categorical columns we will one hot encode
    columns_to_one_hot = ["BORO", "CUISINE DESCRIPTION", "Community Board", "Council District", "Census Tract"]
    # static columns we won't change but want to keep
    static_columns = ["DBA", "CRITICAL"]

    # get the reduced df with only these columns
    reduced_df = violations_df[static_columns + columns_to_one_hot].copy()

    # merge the reduced df with the income df and drop the neighbourhood column sine 
    # it is the same as boro from the reduced
    pre_final_df = pd.merge(reduced_df, income_df, left_on='BORO', right_on='Neighbourhood', how='inner')
    pre_final_df.drop(["Neighbourhood"], axis=1, inplace=True)
    # print(pre_final_df)

    # one hot encode the determined columns
    final_df = pd.get_dummies(reduced_df, columns=columns_to_one_hot, dtype=int)

    print(final_df)
    return final_df

def model_1():

    df = get_model_1_data()

    features = df.drop(["DBA", "CRITICAL"], axis=1)
    # print(features.columns["MEDIAN_INCOME"])
    target = df["CRITICAL"]

    logistic = LogisticRegression(max_iter=1000, C=0.1)
    kfold = KFold(n_splits=10, shuffle=True, random_state=37)

    scorers = {
        'accuracy': make_scorer(accuracy_score),
        'precision': make_scorer(precision_score),
        'recall': make_scorer(recall_score),
        'f1': make_scorer(f1_score)
    }

    results = {name: cross_val_score(logistic, features, target, cv=kfold, scoring=scorer) for name, scorer in scorers.items()}

    # Calculate average scores and standard deviations
    summary = {name: (np.mean(scores), np.std(scores)) for name, scores in results.items()}

    # Display results
    print("K-Fold Validation Results:")
    for metric, (mean, std_dev) in summary.items():
        print(f"{metric.capitalize()}: {mean:.4f} ± {std_dev:.4f}")
    return logistic


def get_burough_from_zip(zipcode):
    Manhattan_start = 10001
    Manhattan_stop = 10282
    StIsl_start = 10301
    StIsl_stop = 10314
    Bronx_start = 10451
    Bronx_stop = 10475
    Queens_start_1 = 11004
    Queens_stop_1 = 11109
    Queens_start_2 = 11351
    Queens_stop_2 = 11697
    Brooklyn_start = 11201
    Brookuln_stop = 11256

    if Manhattan_start <= zipcode <= Manhattan_stop:
        return "Manhattan"
    elif StIsl_start <= zipcode <= StIsl_stop:
        return "Staten Island"
    elif Bronx_start <= zipcode <= Bronx_stop:
        return "Bronx"
    elif Queens_start_1 <= zipcode <= Queens_stop_1 or \
        Queens_start_2 <= zipcode <= Queens_stop_2:
        return "Queens"
    elif Brooklyn_start <= zipcode <= Brookuln_stop:
        return "Brooklyn"
    else:
        return "BAD"



def get_model_2_data():

    rating_df = pd.read_csv("../data_deliverable/Clean/Cleaned Restaurant data.csv")
    rating_selected_cols = ["Name", "Rating", "Price Category", "ZipCode"]
    rating_df = rating_df[rating_selected_cols].dropna(subset=["Rating", "Price Category", "ZipCode"])
    rating_df["Name"] = rating_df["Name"].str.lower()
    # print(rating_df)
    # rating_df["Rating"] = round(rating_df["Rating"]).astype(int)
    rating_df["Price Category"] = rating_df["Price Category"].astype(int)
    rating_df["Burough"] = rating_df["ZipCode"].apply(lambda x: get_burough_from_zip(x))

    clean_df = rating_df.query('Burough != "BAD"')
    # bad_df = rating_df.query('Burough == "BAD"')
    # print(clean_df)
    # print(bad_df)

    income_df = pd.read_csv("../data_deliverable/Clean/Median Incomes 2021 Clean.csv") 
    income_df.rename(columns={"Median Household Income 2021": "MEDIAN_INCOME"}, inplace=True)

    final_df = pd.merge(left=clean_df, right=income_df, left_on="Burough", right_on="Neighbourhood", how="inner")
    final_df.drop(["Neighbourhood"], inplace=True, axis=1)

    # grouped_count = final_df.groupby("Burough").size()
    # print(grouped_count)
    final_df = pd.get_dummies(final_df, columns=["Burough"])
    print(final_df)
    # print(final_df.columns)


    # violation_df = pd.read_excel("../data_deliverable/Clean/violations clean.xlsx")
    # violation_selected_cols = ["DBA", "BORO", "CUISINE DESCRIPTION", "CRITICAL FLAG"]
    # violation_df = violation_df[violation_selected_cols].dropna(subset=violation_selected_cols)
    # violation_df["DBA"] = violation_df["DBA"].str.lower()
    # print(violation_df)

    # merged_df = pd.merge(left=rating_df, right=violation_df, left_on="Name", right_on="DBA", how="inner")
    # print(merged_df)

    return final_df

def model_2():
    df = get_model_2_data()
    # print(df)
    # grouped_count = df.groupby("Rating").size()
    # print(grouped_count)

    features = df.drop(["Name", "Rating", "ZipCode"], axis=1)
    target = df["Rating"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)
    # X_scaled = features

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, target, test_size=0.2, random_state=37, shuffle=True)
    k = 10
    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(X_train, y_train)

    # cross validation
    cv_scores = cross_val_score(knn, X_scaled, target, cv=10)  # 10-fold cross-validation

    print("Cross-Validation Scores:", cv_scores)
    print("Mean Cross-Validation Score:", cv_scores.mean())

    # do on testing set
    y_pred = knn.predict(X_test)

    # evaluate performance
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy on Test Set:", accuracy)

    return knn


if __name__ == "__main__":
    model_1()
    model_2()

