class Room:
    def __init__(self, number, seating_capacity):
        self._number = number
        self._seating_capacity = seating_capacity
    
    def get_number(self):
        return self._number
    
    def get_seating_capacity(self):
        return self._seating_capacity