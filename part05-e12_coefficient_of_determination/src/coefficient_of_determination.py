#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    # Load the data and seperate by tab
    data_frame = pd.read_csv('src/mystery_data.tsv', sep='\t')

    # Different dataframes for X's and Y's columns
    x = data_frame.loc[:, 'X1':'X5']
    y = data_frame.loc[:, 'Y']

    # Create linear regression model
    model = linear_model.LinearRegression(fit_intercept=True)

    # Train model
    model.fit(x, y)
    score = model.score(x, y)

    scores = [score]

    for i in range(len(x.columns)):
        a = x.iloc[:, i].values.reshape(-1, 1)
        model.fit(a, y)
        scores.append(model.score(a, y))

    return scores


def main():
    x = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {x[0]}")
    for i in range(1, len(x)):
        print(f"R2-score with feature(s) X{i}: {x[i]}")


if __name__ == "__main__":
    main()

