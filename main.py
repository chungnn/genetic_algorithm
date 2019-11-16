import random as rnd
import prettytable as prettytable
from data import *
from school_class import *
from schedule import *
from population import *
from display_manager import *
from genetic_algorithm import *

POPULATION_SIZE = 9


data = Data()
display_mgr = DisplayMgr(data)
display_mgr.print_available_data()
generation_number = 0
print("\n> Generation # "  + str(generation_number))
population = Population(POPULATION_SIZE, data)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
display_mgr.print_generation(population)
display_mgr.print_schedule_as_table(population.get_schedules()[0])

GA =  GeneticAlgorithm(data)
while population.get_schedules()[0].get_fitness() != 1.0:
    generation_number += 1
    print("\n> Generation # " + str(generation_number))
    population = GA.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    display_mgr.print_generation(population)
    display_mgr.print_schedule_as_table(population.get_schedules()[0])
print("\n\n")