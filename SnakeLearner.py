import random
import SnakeGame
import tensorflow as tf
from tensorflow import keras

class LearnerPopulationManager:
    '''
    An object that manages SnakeLearners using genetic and evolutionary algorithms
    '''

    def __init__(self):
        pass

class SnakeLearner:
    '''
    An individual member of the LearnerPopulationManager
    A neural network that learns how to play snake
    '''

    # The possible neural network parameters; the ones that get used by SnakeLearners is fine tuned by the LearnerPopulationManager
    network_parameter_choices = {
        "number_neurons": [64, 128, 256],
        "number_layers": [1, 2, 3, 4],
        "activation": ['relu', 'elu'],
        "optimizer": ['rmsprop', 'adam'],
        "number_episodes": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    }

    def __init__(self, network_parameters = None):
        '''
        Compiles a neural network using the given input network parameters
        '''
        self.model = keras.models.Sequential()

        self.network_parameters = network_parameters
        if self.network_parameters == None:
            self.network_parameters = {}
            for key in self.network_parameter_choices:
                self.network_parameters[key] = random.choice(self.network_parameter_choices[key])

        for i in range(self.network_parameters["number_layers"]):
            if i == 0:
                self.model.add(keras.layers.Dense(self.network_parameters["number_neurons"], activation=self.network_parameters["activation"], input_shape=(1,)))
            else:
                self.model.add(keras.layers.Dense(self.network_parameters["number_neurons"], activation=self.network_parameters["activation"]))
        self.model.add(keras.layers.Dense(4, activation="softmax"))

        self.model.compile(loss="mse", optimizer=self.network_parameters["optimizer"])

    def train(self):
        '''
        Trains the neural network based on the network parameters and then runs the test runs where a fitness score is returned
        Fitness score is the average score of all the test runs (not training runs)
        '''
        for _ in range(self.network_parameters["number_episodes"]):
            game = SnakeGame.SnakeGame()
            while True:
                break # TODO: train

        test_scores = []
        for _ in range(5):
            game = SnakeGame.SnakeGame()
            while True:
                predictions = self.model.predict(game.get_state())[0].tolist()
                move = predictions.index(max(predictions))
                game.queue_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]][move]
                if not game.step():
                    test_scores.append(game.score)
                    break
        return sum(test_scores) / len(test_scores)
