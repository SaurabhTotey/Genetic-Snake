import numpy as np
import random
import SnakeGame
import tensorflow as tf
from tensorflow import keras

max_turns_allowed = 5000

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
        "activation": ['relu', 'elu', 'linear'],
        "optimizer": ['rmsprop', 'adam'],
        "number_episodes": [5 * (i + 1) for i in range(200)]
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
                self.model.add(keras.layers.Dense(self.network_parameters["number_neurons"], activation=self.network_parameters["activation"], input_shape=(705,)))
            else:
                self.model.add(keras.layers.Dense(self.network_parameters["number_neurons"], activation=self.network_parameters["activation"]))
        self.model.add(keras.layers.Dense(1, activation="linear"))

        self.model.compile(loss="mse", optimizer=self.network_parameters["optimizer"])

    def train(self):
        '''
        Trains the neural network based on the network parameters and then runs the test runs where a fitness score is returned
        Fitness score is the average score of all the test runs (not training runs)
        '''
        exploration_rate = 1
        for _ in range(self.network_parameters["number_episodes"]):
            game = SnakeGame.SnakeGame()
            move = -1
            for _ in range(max_turns_allowed):
                if random.random() < exploration_rate:
                    move = random.choice(range(4))
                    exploration_rate *= 0.9
                else:
                    predictions = [self.model.predict(np.array([i] + game.get_state()).reshape(-1, 705), verbose=0).tolist()[0][0] for i in range(4)]
                    move = predictions.index(max(predictions))
                game.queue_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]][move]
                previous_score = game.score
                previous_apple_location = [game.apple_X, game.apple_Y]
                is_alive = game.step()
                reward = game.score - previous_score
                if not is_alive:
                    reward = -100
                elif [game.apple_X, game.apple_Y] != previous_apple_location:
                    reward = 100
                self.model.fit(np.array([move] + game.get_state()).reshape(-1, 705), np.array([reward]), verbose=0)
                if not is_alive:
                    break

        test_scores = []
        for _ in range(5):
            game = SnakeGame.SnakeGame()
            for _ in range(max_turns_allowed):
                predictions = [self.model.predict(np.array([i] + game.get_state()).reshape(-1, 705), verbose=0).tolist()[0][0] for i in range(4)]
                move = predictions.index(max(predictions))
                print(str(predictions) + ": " + str(move))
                game.queue_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]][move]
                if not game.step():
                    test_scores.append(game.score)
                    break
        return sum(test_scores) / len(test_scores)
