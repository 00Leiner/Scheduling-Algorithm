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

  csp_solver = csp.CSPAlgorithm(students, courses, teachers, rooms)
  result = csp_solver.backtracking_search(2) # the value is the number of options or solutions you want
  for teacher_id in result:
    for r in teacher_id:
      print(r)