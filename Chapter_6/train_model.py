import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import joblib


def parse_arguments():
    parser = argparse.ArgumentParser(description="Directory of the .csv file that you wish to train the model with.")

    parser.add_argument("-f", "--file", type=str, help="Directory of the .csv file that you wish to use to train the "
                                                       "model.")

    arguments = parser.parse_args()
    file = arguments.file

    return file


def main(file):
    print("Hello, World: You are running train_model_pt4.py")

    # Load the dataset.
    df = pd.read_csv(file)

    # Preprocess the data.

    # Remove the fields from the dataset that we do not want to include in the final model.
    del df['house_number']
    del df['unit_number']
    del df['street_name']
    del df['zip_code']

    # Remove categorical columns with one-hot encoded data.
    features_df = pd.get_dummies(df, columns=['garage_type', 'city'])

    # Remove the sale price column from the feature dataset (this is the column that we want to predict).
    sale_price = df['sale_price']
    del df['sale_price']

    # Create X and Y arrays for inputting to the model.
    X = features_df.to_numpy()
    Y = sale_price.to_numpy()

    # Split data into training and testing sets with a 70%/30% split.
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.3)

    # Fit regression model.
    model = ensemble.GradientBoostingRegressor(
        n_estimators=1000,
        learning_rate=.1,
        max_depth=6,
        min_samples_leaf=9,
        max_features=.1,
        loss='huber'
    )

    model.fit(X_train, Y_train)

    # Save the trained model to file so that it can be used within other programs.
    joblib.dump(model, 'trained_house_classifier_model.pkl')

    # Find the training data set model error rate.
    mse_train = mean_absolute_error(Y_train, model.predict(X_train))
    print(f"Training data set mean absolute error: {mse_train}")

    # Find the test dataset model error rate.
    mse_test = mean_absolute_error(Y_test, model.predict(X_test))
    print(f"Testing data set mean absolute error: {mse_test}")


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
