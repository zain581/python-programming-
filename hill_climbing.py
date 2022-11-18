from random import randint
from random import *
import math
class hill_climbing:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.path = []
        self.path_cost = 0
        self.goal_test(self.start_state)
        self.path.append(self.start_state)
        self.path_cost += self.start_state.cost
        self.path.append(self.goal_state)
        self.path_cost += self.goal_state.cost
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False
    def successor_function(self, state):
        successors = []
        for i in range(len(state.neighbors)):
            if state.neighbors[i].cost < state.cost:
                successors.append(state.neighbors[i])
        return successors
    def best_successor(self, successors):
        best_successor = successors[0]
        for i in range(len(successors)):
            if successors[i].cost < best_successor.cost:
                best_successor = successors[i]
        return best_successor
    def search(self):
        while self.goal_test(self.start_state) == False:
            successors = self.successor_function(self.start_state)
            best_successor = self.best_successor(successors)
            self.start_state = best_successor
            self.path.append(best_successor)
            self.path_cost += best_successor.cost
    def print_path(self):
        print("Path:")
        for i in range(len(self.path)):
            print(self.path[i].name)
        print("Path cost:")
        print(self.path_cost)
def hill_climb(start_state, goal_state):
    hc = hill_climb(start_state, goal_state)
    hc.search()
    hc.print_path()
class simulated_annealing:
    def __init__(self, start_state, goal_state, temp):
        self.start_state = start_state
        self.goal_state = goal_state
        self.temp = temp
        self.path = []
        self.path_cost = 0
        self.goal_test(self.start_state)
        self.path.append(self.start_state)
        self.path_cost += self.start_state.cost
        self.path.append(self.goal_state)
        self.path_cost += self.goal_state.cost
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False
    def successor_function(self, state):
        successors = []
        for i in range(len(state.neighbors)):
            if state.neighbors[i].cost < state.cost:
                successors.append(state.neighbors[i])
        return successors
    def best_successor(self, successors):
        best_successor = successors[0]
        for i in range(len(successors)):
            if successors[i].cost < best_successor.cost:
                best_successor = successors[i]
        return best_successor
    def search(self):
        while self.goal_test(self.start_state) == False:
            successors = self.successor_function(self.start_state)
            best_successor = self.best_successor(successors)
            delta_cost = best_successor.cost - self.start_state.cost
            if delta_cost < 0:
                self.start_state = best_successor
                self.path.append(best_successor)
                self.path_cost += best_successor.cost
            else:
                prob = math.exp(-delta_cost/self.temp)
                if random.random() < prob:
                    self.start_state = best_successor
                    self.path.append(best_successor)
                    self.path_cost += best_successor.cost
class beam_search:
    def __init__(self, start_state, goal_state, beam_width):
        self.start_state = start_state
        self.goal_state = goal_state
        self.beam_width = beam_width
        self.path = []
        self.path_cost = 0
        self.goal_test(self.start_state)
        self.path.append(self.start_state)
        self.path_cost += self.start_state.cost
        self.path.append(self.goal_state)
        self.path_cost += self.goal_state.cost
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False
    def successor_function(self, state):
        successors = []
        for i in range(len(state.neighbors)):
            if state.neighbors[i].cost < state.cost:
                successors.append(state.neighbors[i])
        return successors
    def best_successor(self, successors):
        best_successor = successors[0]
        for i in range(len(successors)):
            if successors[i].cost < best_successor.cost:
                best_successor = successors[i]
        return best_successor
    def beam_search(self):
        while self.goal_test(self.start_state) == False:
            successors = self.successor_function(self.start_state)
            best_successors = []
            for i in range(self.beam_width):
                best_successors.append(self.best_successor(successors))
            self.start_state = best_successors[0]
            self.path.append(best_successors[0])
            self.path_cost += best_successors[0].cost
    def print_path(self):
        print("Path:")
        for i in range(len(self.path)):
            print(self.path[i].name)
        print("Path cost:")
        print(self.path_cost)
