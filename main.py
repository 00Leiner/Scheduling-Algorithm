import csp
from _data.student_data import fetch_student_data
from _data.room_data import fetch_room_data
from _data.teacher_data import fetch_teacher_data
from _data.course_data import fetch_course_data


if __name__ == "__main__":
  students = fetch_student_data()
  courses = fetch_course_data()
  teachers = fetch_teacher_data()
  rooms = fetch_room_data()
  '''
  students = data.students
  courses = data.courses
  teachers = data.teachers
  rooms = data.rooms
'''
  #scheduling.Scheduling(students, courses, teachers, rooms)
  csp.CSPAlgorithm(students, courses, teachers, rooms)