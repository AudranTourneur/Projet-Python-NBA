import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, metrics
from player_data import create_players_dataset
from sklearn.model_selection import train_test_split


def compare_test_and_prediction(y_test, y_pred):
    # We are going to compare the actual values of y_test with the predicted values of y_pred
    # in a loop
    # Note: the indexes might not match

    # Let's compare the number of correct predictions with the total number of predictions
    # We will consider a prediction correct if the difference between the actual value and the predicted value is less than 20%
    tolerance = 0.1
    correct = 0
    # iterate over y_test the Pandas way
    pred_index = 0
    for index, value in y_test.items():
        print("Actual value =", value, "Predicted value =", y_pred[pred_index])
        if abs(value - y_pred[pred_index]) <= tolerance:
            correct += 1
        pred_index += 1

    print("Correct predictions =", correct)
    print("Total predictions =", len(y_test))
    print("Accuracy =", correct / len(y_test))


def train_model():
    df = create_players_dataset()

    # Let's split the dataset in 80% / 20% for training and testing
    # We will use the first 80% for training and the last 20% for testing

    print(df)

    # drop PLAYER_ID
    df = df.drop('PLAYER_ID', axis=1)

    # drop POSITION
    df = df.drop('POSITION', axis=1)

    # print columns
    print(df.columns)

    x_input_data = df[['FGM', 'AST', 'REB', 'FGA', 'PF']]
    y_output = df['WinRate']

    X_train, X_test, y_train, y_test = train_test_split(x_input_data, y_output, test_size=0.2,
                                                        random_state=42)

    print("X_train", X_train)

    print("X_test", X_test)

    print("y_train", y_train)

    print("y_test", y_test)

    # Let's train the model
    logreg = linear_model.LinearRegression()
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)

    print("predictions", y_pred)

    print("Actual values =", y_test)

    # Evaluate the model
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    print('test', len(y_test))
    print('pred', len(y_pred))

    compare_test_and_prediction(y_test, y_pred)

    # visualize
    plt.clf()
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.savefig('scatter_ai.png')


train_model()
