from room import *
from department import *
from course import *
from meeting_time import *
from instructor import *

class Data:
    ROOMS = [["R1", 25], ["R2", 45], ["R3", 35]]
    MEETING_TIMES = [
        ["MT1", "08:00 - 09:45"],
        ["MT2", "10:00 - 11:45"],
        ["MT3", "12:00 - 13:45"],
        ["MT4", "14:30 - 16:00"]
    ]
    INSTRUCTORS = [
        ["I1", "Dr James Web"],
        ["I2", "Mr. Mike Brown"],
        ["I3", "Dr Steve Day"],
        ["I4", "Mrs Jane Dow"]
    ]
    def __init__(self):
        self._rooms = []
        self._meeting_times = []
        self._instructors = []
        for i in range(len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(len(self.MEETING_TIMES)):
            self._meeting_times.append(MettingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        course1 = Course("C1", "Statistic", [self._instructors[0], self._instructors[1]], 25)
        course2 = Course("C2", "OOP", [self._instructors[0], self._instructors[1], self._instructors[2]], 35)
        course3 = Course("C3", "Discrete Math", [self._instructors[0], self._instructors[1]], 25)
        course4 = Course("C4", "Datase", [self._instructors[2], self._instructors[3]], 30)
        course5 = Course("C5", "AI", [self._instructors[3]], 35)
        course6 = Course("C6", "Atomic Physic", [self._instructors[0], self._instructors[2]], 45)
        course7 = Course("C7", "Mechanicak", [self._instructors[1], self._instructors[3]], 45)
        self._courses = [course1, course2, course3, course4, course5, course6, course7]
        dept1 = Department("MATH", [course1, course3])
        dept2 = Department("PRO", [course2, course4, course5])
        dept3 = Department("PHY", [course6, course7])
        self._depts = [dept1, dept2, dept3]
        self._number_of_classes = 0
        for i in range(len(self._depts)):
            self._number_of_classes += len(self._depts[i].get_courses())
        
    def get_rooms(self):
        return self._rooms
    
    def get_instructors(self):
        return self._instructors
    
    def get_courses(self):
        return self._courses
    
    def get_depts(self):
        return self._depts
    
    def get_meetings_times(self):
        return self._meeting_times
    
    def get_number_of_classes(self):
        return self._number_of_classes
