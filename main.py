import SnakeGame
import SnakeGui
import SnakeLearner

if __name__ == '__main__':
    # SnakeGui.SnakeWindow(SnakeGame.SnakeGame(), None)
    learner = SnakeLearner.GeneticLearner()
    for i in range(15):
        print("Generation " + str(i) + ": " + str(learner.fitness_of(learner.best_of_generation())))
