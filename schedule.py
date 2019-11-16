from school_class import *
import random as rnd

class Schedule:
    def __init__(self, data):
        self._data = data
        self._classes = []
        self._number_of_conficts = 0
        self._fitness = -1
        self._class_numb = 0
        self._is_fitness_changed = True
    
    def get_classes(self):
        self._is_fitness_changed = True
        return self._classes
    
    def get_number_of_conflicts(self):
        return self._number_of_conficts
    
    def get_fitness(self):
        if self._is_fitness_changed:
            self._fitness = self.caculate_fitness()
            self._is_fitness_changed = False
        return self._fitness

    def initialize(self):
        data = self._data
        depts = self._data.get_depts()
        for i in range(len(depts)):
            courses = depts[i].get_courses()
            for j in range(len(courses)):
                new_class = SchoolClass(self._class_numb, depts[i], courses[j])
                self._class_numb += 1
                new_class.set_meeting_time(data.get_meetings_times()[rnd.randrange(0, len(data.get_meetings_times()))])
                new_class.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                new_class.set_instructor(courses[j].get_instructor()[rnd.randrange(0, len(courses[j].get_instructor()))])
                self._classes.append(new_class)
        return self

    def caculate_fitness(self):
        self._number_of_conficts = 0
        classes = self.get_classes()
        for i in range(len(classes)):
            if classes[i].get_room().get_seating_capacity() < classes[i].get_course().get_max_number_student():
                self._number_of_conficts += 1
            for j in range(len(classes)):
                if j > i:
                    if classes[i].get_meeting_time() == classes[j].get_meeting_time() and classes[i].get_id() != classes[j].get_id():
                        if classes[i].get_room() == classes[j].get_room():
                            self._number_of_conficts += 1
                        if classes[i].get_instructor() == classes[j].get_instructor():
                            self._number_of_conficts += 1
        return 1 / ((1.0 * self._number_of_conficts + 1))
    

    def __str__(self):
        returnValue = ""
        for i in range(len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue
