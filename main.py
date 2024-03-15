import requests
from flask import Flask, jsonify
from csp import CSPAlgorithm
from _data.student_data import fetch_student_data
from _data.room_data import fetch_room_data
from _data.teacher_data import fetch_teacher_data
from _data.course_data import fetch_course_data

app = Flask(__name__)


class Fetching:
    def __init__(self):
        self.url = 'http://172.31.4.61:3000/Schedule/create'

    def perform_post_request(self, data):
        response = requests.post(self.url, json=data)

        if response.status_code in [200, 201]:
            return response
        else:
            print(f"Error in POST request. Status code: {response.status_code}")
            print(response.text)
            return response

@app.route('/activate_csp_algorithm', methods=['POST'])
def activate_csp_algorithm():
    try:
      students = fetch_student_data()
      courses = fetch_course_data()
      teachers = fetch_teacher_data()
      rooms = fetch_room_data()
      
      csp_solver = CSPAlgorithm(students, courses, teachers, rooms)
      result = csp_solver.backtracking_search() 

      print(f'Number of solutions found!')

      fetching_instance = Fetching()
      for solution in result:
          response = fetching_instance.perform_post_request(solution)
          print(response.text)

      return jsonify({"status": "success", "message": "CSP algorithm activated successfully"})
    except Exception as e:
      return jsonify({"status": "error", "message": str(e)})
    


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)