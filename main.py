import SnakeGame
import SnakeGui
import SnakeLearner
import numpy as np

#Set learner to None to play Snake manually
learner = None #SnakeLearner.SnakeLearner()

training_episodes = 500

if __name__ == '__main__':
    if learner != None:
        for i in range(training_episodes):
            pass
    SnakeGui.SnakeWindow(SnakeGame.SnakeGame(), learner)
