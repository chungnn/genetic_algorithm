class Course:
    def __init__(self, number, name, instructor, max_number_student):
        self._number = number
        self._name = name
        self._instructor = instructor
        self._max_number_student = max_number_student
    
    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_instructor(self):
        return self._instructor

    def get_max_number_student(self):
        return self._max_number_student
    

    def __str__(self):
        return self._name 
