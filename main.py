import SnakeGame
import SnakeGui
import SnakeLearner

if __name__ == '__main__':
    SnakeGui.SnakeWindow(SnakeGame.SnakeGame(), SnakeLearner.GeneticLearner())
