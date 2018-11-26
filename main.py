import SnakeGame
import SnakeGui
import SnakeLearner

if __name__ == '__main__':
    learner = SnakeLearner.SnakeLearner()
    print(str(learner.network_parameters) + ": " + str(learner.train()))
    # SnakeGui.SnakeWindow(SnakeGame.SnakeGame(), None)
