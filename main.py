import requests
from flask import Flask, jsonify
from csp import CSPAlgorithm
from _data.student_data import fetch_student_data
from _data.room_data import fetch_room_data
from _data.teacher_data import fetch_teacher_data
from _data.course_data import fetch_course_data
from _data_format.data_format import formatting_data

app = Flask(__name__)


def main():
    students = fetch_student_data()
    courses = fetch_course_data()
    teachers = fetch_teacher_data()
    rooms = fetch_room_data()

    csp_solver = CSPAlgorithm(students, courses, teachers, rooms)
    result = csp_solver.backtracking_search() 
    return result


@app.route('/activate_csp_algorithm', methods=['POST'])
def activate_csp_algorithm():
    try:
        formatted_data = main()
        
        # Post data to the database endpoint
        database_url = 'http://ec2-13-54-170-228.ap-southeast-2.compute.amazonaws.com:3000/Schedule/create'
        response = requests.post(database_url, json=formatted_data)

        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Data posted to database successfully"})
        else:
            return jsonify({"status": "error", "message": f"Failed to post data to database. Status code: {response.status_code}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)