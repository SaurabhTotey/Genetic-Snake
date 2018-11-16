import SnakeGame
import SnakeGui
import SnakeLearner
import copy

#Set learner to None to play Snake manually
learner = SnakeLearner.SnakeLearner()

training_episodes = 500

if __name__ == '__main__':
    if learner != None:
        for i in range(training_episodes):
            game = SnakeGame.SnakeGame()
            is_alive = True
            while is_alive:
                initial = copy.copy(game)
                move, reward, is_alive = learner.make_move(game.get_state())
                learner.train(initial, move, reward, not is_alive)
    SnakeGui.SnakeWindow(SnakeGame.SnakeGame(), learner)
