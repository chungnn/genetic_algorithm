from schedule import *

class Population:
    def __init__(self, size, data):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(size):
            self._schedules.append(Schedule(self._data).initialize())
    
    def get_schedules(self):
        return self._schedules