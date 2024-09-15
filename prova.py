import keras
import sklearn
import time

def main() :
    model = keras.Sequential(
        layers = [
            keras.Input((2,)),
            keras.layers.Dense(128),
            keras.layers.Dense(128),
            keras.layers.Dense(3, activation = None)
        ]
    )
    model.compile(loss = keras.losses.mean_squared_error)

    input = [
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ]

    output = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    for _ in range(0, 1_000) :
        model.train_on_batch(input, output)

