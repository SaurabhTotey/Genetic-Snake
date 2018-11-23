import SnakeGame
import SnakeGui
import SnakeLearner

if __name__ == '__main__':
    learner = SnakeLearner.SnakeLearner()
    print(learner.train())
