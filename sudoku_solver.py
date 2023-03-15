# required imports
import numpy as np
import random

class solver():
    
    def __init__(self):
        '''
        Initialize the sudoku game with only the values provided. Also create an initial
        population of randomly completed boards.
        '''
        
        self.board = board
        self.memory = set()
        
        # find all zeros (blanks) on the board
        x,y = np.where(self.board==0)
        self.zeros = list(zip(x,y))

        board_len = self.board.shape[0]
        self.best_fitness = board_len*(board_len-1)*3
        
        self.pop = build_pop(init_board, zeros, 100)
        self.pop = evaluation(self.pop)
        
        
    
    def solve(self):
        '''
        Start solving the sudoku game using a genetic algorithm.
        '''
        
        i = 0
        while self.best_fitness > 0:

            mutation_rate = 1.0
        #     if best_fitness >= 15:
        #         mutation_rate = .3
        #     if best_fitness > 10:
        #         mutation_rate = .5
        #     else:
        #         mutation_rate = .6

            self.pop = self.selection(self.pop)
        #     pop = crossover(pop, p_dist, elitism=elitism)
            self.pop = self.crossover(self.pop, p_dist, elitism=True)
            self.pop = self.mutation(self.pop, mutation_rate, zeros)
        #     pop = mutation(pop,.3,zeros)
            self.pop = self.evaluation(self.pop)

            if i % 500 == 0:
                f = [self.fitness(b) for b in self.pop]
                f = np.array(f)
                print(f'Averge board fitness at {i} = {np.average(f)}')

            if self.fitness(self.pop[0]) < self.best_fitness:
                self.best_fitness = self.fitness(self.pop[0])
                print(f"New best fitness: {self.best_fitness} | i={i}")
            i+=1