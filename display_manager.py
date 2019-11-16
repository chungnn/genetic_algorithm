import prettytable as prettytable

class DisplayMgr:
    def __init__(self, data):
        self._data = data

    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_dept(self):
        data = self._data
        depts = data.get_depts()
        availabel_depts_table = prettytable.PrettyTable(['dept', 'course'])
        for i in range(len(depts)):
            courses = depts.__getitem__(i).get_courses()
            temp_str = "["
            for j in range(len(courses) - 1):
                temp_str += courses[j].__str__() + ", "
            temp_str += courses[len(courses) - 1].__str__() + "]"
            availabel_depts_table.add_row([depts.__getitem__(i).get_name(), temp_str])
        print(availabel_depts_table)
    
    def print_course(self):
        data = self._data
        availabel_course_table = prettytable.PrettyTable(['id', 'course #', 'max # of students', 'instructors'])
        courses = data.get_courses()
        for i in range(len(courses)):
            instructors = courses[i].get_instructor()
            tmp_str = ""
            for j in range(len(instructors) - 1):
                tmp_str += instructors[j].__str__() + ", "
            tmp_str += instructors[len(instructors) - 1].__str__()
            availabel_course_table.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_max_number_student()), tmp_str]
            )
        print(availabel_course_table)
    
    def print_instructor(self):
        data = self._data
        availabel_instructor_table = prettytable.PrettyTable(['id', 'instructor'])
        instructors = data.get_instructors()
        for i in range(len(instructors)):
            availabel_instructor_table.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availabel_instructor_table)
    
    def print_room(self):
        data = self._data
        available_room_table = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(len(rooms)):
            available_room_table.add_row([str(rooms[i].get_number()), str(rooms[i].get_seating_capacity())])
        print(available_room_table)
    
    def print_meeting_times(self):
        data = self._data
        availabel_meeting_time_table = prettytable.PrettyTable(['id', 'Meeting Time'])
        meeting_times = data.get_meetings_times()
        for i in range(len(meeting_times)):
            availabel_meeting_time_table.add_row([meeting_times[i].get_id(), meeting_times[i].get_time()])
        print(availabel_meeting_time_table)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflict', 'classes []'])
        schedules = population.get_schedules()
        for i in range(len(schedules)):
            table1.add_row([str(i),
            round(schedules[i].get_fitness(), 3),
            schedules[i].get_number_of_conflicts(), schedules[i]
        ])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(['Class #', 'Dept', 'Course (number, max # of student)', 'Room (capacity)', 'Instructor', 'times'])
        for i in range(len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" + 
            classes[i].get_course().get_number() + ", " + 
            str(classes[i].get_course().get_max_number_student()) + ")",
            classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_seating_capacity()),
            classes[i].get_instructor().get_name() + " (" + str(classes[i].get_instructor().get_id()) + ")",
            classes[i].get_meeting_time().get_time() + " (" + str(classes[i].get_meeting_time().get_id()) + ")"
            ])
        print(table)