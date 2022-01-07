import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers


def train_model():
    dataset = np.load("./dataset/result_based_dataset_100k.npz")

    X = dataset["arr_0"]
    Y = dataset["arr_1"]
    # X_n = keras.utils.normalize(X, axis=-1)
    # Y_n = keras.utils.normalize(Y, axis=-1)[0]

    """
    plt.figure()
    plt.hist(Y)
    plt.show()
    exit(0)
    """
    
    model = keras.Sequential([
        layers.Dense(128, input_dim=64, activation="relu"),
        layers.Dense(64, activation="relu"),
        layers.Dense(1, activation="tanh")
    ])
    
    model.compile(loss="mean_squared_error", optimizer=keras.optimizers.Adam(0.001), metrics=["accuracy"])
    model.predict(X[:10])
    print(model.summary())
    
    history = model.fit(X, Y, validation_split=0.2, epochs=10, shuffle=True)
    
    # prediction = model.predict(X[:50])

    model.save("./neural_weights")


if __name__ == "__main__":
    train_model()
