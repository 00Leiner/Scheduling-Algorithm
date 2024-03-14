import csp
from _data.student_data import fetch_student_data
from _data.room_data import fetch_room_data
from _data.teacher_data import fetch_teacher_data
from _data.course_data import fetch_course_data
from _data_format.data_format import formatting_data

class Main:
  def __init__(self):
        self.students = fetch_student_data()
        self.courses = fetch_course_data()
        self.teachers = fetch_teacher_data()
        self.rooms = fetch_room_data()

        self.csp_solver = csp.CSPAlgorithm(self.students, self.courses, self.teachers, self.rooms)
        self.result = self.csp_solver.backtracking_search()  
        #print(self.result)
        self.student_details = {student['_id']: student for student in self.students}
        self.course_details = {course['code']: course for course in self.courses}
        self.teacher_details = {teacher['_id']: teacher for teacher in self.teachers}
        self.room_details = {room['_id']: room for room in self.rooms}

        _data = formatting_data(self.result, self.student_details, self.course_details, self.teacher_details, self.room_details)
        print(_data)

  
Main()