from population import *

POPULATION_SIZE = 9
NUMBER_OF_ELITE_SCHEDULES = 1
TOURAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1

class GeneticAlgorithm:
    def __init__(self, data):
        self._data = data

    def evolve(self, population):
        return self._mutable_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0, self._data)
        for i in range(NUMBER_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMBER_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tourament_population(pop).get_schedules()[0]
            schedule2 = self._select_tourament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop
    
    def _mutable_population(self, population):
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutable_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        cross_schedule = Schedule(self._data).initialize()
        for i in range(len(cross_schedule.get_classes())):
            if rnd.random() > 0.5:
                cross_schedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                cross_schedule.get_classes()[i] = schedule2.get_classes()[i]
        return cross_schedule

    def _mutable_schedule(self, mutable_schedule):
        schedule = Schedule(self._data).initialize()
        for i in range(len(mutable_schedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutable_schedule.get_classes()[i] = schedule.get_classes()[i]
        return mutable_schedule

    def _select_tourament_population(self, pop):
        tournament_pop = Population(0, self._data)
        i = 0
        while i < TOURAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop
