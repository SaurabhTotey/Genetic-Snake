import random
import SnakeGame
import statistics

max_turns_allowed = 5000

class GeneticLearner:

    population_size = 1000
    mutation_rate = 0.0001

    def __init__(self):
        self.population = []
        for i in range(self.population_size):
            self.population.append([])
            for _ in range(max_turns_allowed):
                self.population[i].append(random.choice(range(4)))

    def fitness_of(self, moveset):
        game = SnakeGame.SnakeGame()
        for move in moveset:
            game.queue_direction([[0, -1], [0, 1], [-1, 0], [1, 0]][move])
            if game.step():
                break
        return game.score

    def breed(self, m1, m2):
        new_moveset = []
        for i in range(0, max_turns_allowed, 10):
            new_moveset += random.choice([m1[i:i+10], m2[i:i+10]])
        for i in range(max_turns_allowed):
            if random.random() < self.mutation_rate:
                new_moveset[i] = random.choice(range(4))
        return new_moveset

    def best_of_generation(self):
        scores = [self.fitness_of(moveset) for moveset in self.population]
        top_score = max(scores)
        best_scorer = self.population[scores.index(top_score)]

        score_cutoff = statistics.median(scores)

        new_population = []
        new_population.append(best_scorer)

        low_scorers_added = 0
        checking_index = 0
        checking_order = [i for i in range(self.population_size)]
        random.shuffle(checking_order)
        while low_scorers_added < 10:
            index = checking_order[checking_index]
            if scores[index] < score_cutoff:
                low_scorers_added += 1
                new_population.append(self.breed(best_scorer, self.population[index]))
            checking_index += 1

        best_players = [i for i in range(self.population_size) if scores[i] > score_cutoff]
        while len(new_population) < self.population_size:
            index_of_first = random.choice(best_players)
            index_of_second = index_of_first
            while index_of_second == index_of_first:
                index_of_second = random.choice(best_players)
            new_population.append(self.breed(self.population[index_of_first], self.population[index_of_second]))

        self.population = new_population
        return best_scorer
