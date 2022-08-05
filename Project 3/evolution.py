import copy
import numpy as np
import pickle
import random

from player import Player

mutation_prob = 0.3


def get_players_fitness(players):
    players_fitness = []
    for player in players:
        players_fitness.append(player.fitness)
    return players_fitness


def new_fitness_function(fitness_arr):
    new_fitness_arr = []
    for fitness in fitness_arr:
        new_fitness_arr.append(fitness ** 2)

    return new_fitness_arr


def generate_random_uniform():
    return np.random.uniform(0, 1, 1)[0]


def add_noise(matrix, noise):
    # noise = np.random.uniform(-0.5, 0.5, matrix.shape)
    matrix_copy = copy.deepcopy(matrix)
    noise = np.random.normal(0, noise, matrix.shape)
    matrix_copy += noise
    return matrix_copy


def q_tournomant(players, num_players):
    q = 5
    selected = []
    for i in range(num_players):
        players = random.choices(players, k=q)
        max_fitness = 0
        selected_player = None
        for player in players:
            if player.fitness > max_fitness:
                selected_player = player
        selected.append(selected_player)
    return selected


def sus(players, num_players):
    sum_fitness = 0
    selected_players = []

    for p in players:
        sum_fitness += p.fitness
    average = sum_fitness / num_players

    lines = np.arange(num_players, step=average)

    random_number = np.random.uniform(0, average)
    print(random_number)
    lines = lines + random_number
    counter = 0
    while len(selected_players) != num_players:
        for line in lines:
            selected_players.append(players[counter - 1])
            counter += 1
    return selected_players


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"
        # f.close()

    def mutate(self, child):
        # child: an object of class `Player`
        if generate_random_uniform() <= mutation_prob:
            child.nn.w1 = add_noise(child.nn.w1, 0.5)
        if generate_random_uniform() <= mutation_prob:
            child.nn.b1 = add_noise(child.nn.b1, 0.5)
        if generate_random_uniform() <= mutation_prob:
            child.nn.w2 = add_noise(child.nn.w2, 0.5)
        if generate_random_uniform() <= mutation_prob:
            child.nn.b2 = add_noise(child.nn.b2, 0.5)

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)

        # TODO (Additional: Learning curve)
        average = 0
        for p in players:
            average += p.fitness
        players.sort(key=lambda x: x.fitness, reverse=True)
        print(players[0].fitness)
        # print(average/300)
        # print(players[299].fitness)
        # print("\n\n\n\n\n\n")
        f = open("points.txt", "a")
        f.write(str(players[0].fitness) + " " + str(int(average / 300)) + " " + str(players[299].fitness) + "\n")
        # pickle.dump([players[0].fitness, average/300, players[299].fitness], self.f)
        players_fitness_arr = get_players_fitness(players)
        players_new_fitness_arr = new_fitness_function(players_fitness_arr)
        players = random.choices(players, weights=players_new_fitness_arr, k=num_players)

        return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            child_list = []
            players_fitness_arr = get_players_fitness(prev_players)
            players_new_fitness_arr = new_fitness_function(players_fitness_arr)
            prev_players = random.choices(prev_players, weights=players_new_fitness_arr, k=num_players)
            # prev_players = q_tournomant(prev_players, num_players)
            # prev_players = sus(prev_players, num_players)

            for i in range(int(len(prev_players) / 2) - 1):
                # prev_players.sort(key=lambda x: x.fitness, reverse=True)
                # child1, child2 = self.crossover(prev_players[0], prev_players[1])
                child1, child2 = self.crossover(prev_players[i * 2], prev_players[i * 2 + 1])
                # self.mutate(child1)
                # self.mutate(child1)
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)
                child_list.append(child1)
                child_list.append(child2)
            new_players = child_list
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player

    def crossover(self, parent1, parent2):
        parent1_w1 = parent1.nn.w1
        parent1_w2 = parent1.nn.w2
        parent1_b1 = parent1.nn.b1
        parent1_b2 = parent1.nn.b2

        parent2_w1 = parent2.nn.w1
        parent2_w2 = parent2.nn.w2
        parent2_b1 = parent2.nn.b1
        parent2_b2 = parent2.nn.b2

        child1 = self.clone_player(parent1)
        child2 = self.clone_player(parent2)

        for counter, i in enumerate(parent1_w1):
            child1.nn.w1[counter] = np.append(i[0:int(len(i) / 2)], parent2_w1[counter][int(len(i) / 2):len(i)])
            child2.nn.w1[counter] = np.append(parent2_w1[counter][0:int(len(i) / 2)], i[int(len(i) / 2):len(i)])

        for counter, i in enumerate(parent1_w2):
            child1.nn.w2[counter] = np.append(i[0:int(len(i) / 2)], parent2_w2[counter][int(len(i) / 2):len(i)])
            child2.nn.w2[counter] = np.append(parent2_w2[counter][0:int(len(i) / 2)], i[int(len(i) / 2):len(i)])

        child1.nn.b1[0:int(len(parent1_b1) / 2)] = parent1_b1[0:int(len(parent1_b1) / 2)]
        child1.nn.b1[int(len(parent1_b1) / 2):int(len(parent1_b1))] = parent2_b1[
                                                                      int(len(parent1_b1) / 2):int(len(parent1_b1))]
        child2.nn.b1[0:int(len(parent1_b1) / 2)] = parent2_b1[0:int(len(parent1_b1) / 2)]
        child2.nn.b1[int(len(parent1_b1) / 2):int(len(parent1_b1))] = parent1_b1[
                                                                      int(len(parent1_b1) / 2):int(len(parent1_b1))]

        child1.nn.b2[0:int(len(parent1_b2) / 2)] = parent1_b2[0:int(len(parent1_b2) / 2)]
        child1.nn.b2[int(len(parent1_b2) / 2):int(len(parent1_b2))] = parent2_b2[
                                                                      int(len(parent1_b2) / 2):int(len(parent1_b2))]
        child2.nn.b2[0:int(len(parent1_b2) / 2)] = parent2_b2[0:int(len(parent1_b2) / 2)]
        child2.nn.b2[int(len(parent1_b2) / 2):int(len(parent1_b2))] = parent1_b2[
                                                                      int(len(parent1_b2) / 2):int(len(parent1_b2))]

        return child1, child2

    def mutation(self, child):
        child_w1 = child.nn.w1
        child_w2 = child.nn.w2
        child_b1 = child.nn.b1
        child_b2 = child.nn.b2

        new_child = self.clone_player(child)

        if np.random.uniform(0, 1, 1)[0] < mutation_prob:
            new_child.nn.w1 = child_w1 + np.random.randn(10, 6)
        if np.random.uniform(0, 1, 1)[0] < mutation_prob:
            new_child.nn.w2 = child_w2 + np.random.randn(1, 10)
        if np.random.uniform(0, 1, 1)[0] < mutation_prob:
            new_child.nn.b1 = child_b1 + np.random.randn(10, 1)
        if np.random.uniform(0, 1, 1)[0] < mutation_prob:
            new_child.nn.b2 = child_b2 + np.random.randn(1, 1)

        return new_child
