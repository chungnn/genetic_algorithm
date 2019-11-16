class SchoolClass:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meeting_time = None
        self._room = None

    def get_id(self):
        return self._id
    
    def get_dept(self):
        return self._dept
    
    def get_course(self):
        return self._course
    
    def get_instructor(self):
        return self._instructor
    
    def get_meeting_time(self):
        return self._meeting_time
    
    def get_room(self):
        return self._room

    def set_instructor(self, instructor):
        self._instructor = instructor
    
    def set_meeting_time(self, meeting_time):
        self._meeting_time = meeting_time
    
    def set_room(self, room):
        self._room = room
    
    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
            str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(self._meeting_time.get_id())
