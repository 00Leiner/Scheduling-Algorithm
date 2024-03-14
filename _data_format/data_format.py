def formatting_data(result, students_details, courses_details, teachers_details, rooms_details):
    check_same_student = []
    options_counter = 1
    to_format_data = []
    for sched in result:
        formatted_assignment = {
            "options": options_counter,
            "programs": []
        }
        for (student_id, course_code), info in sched.items():
            day1 = info['schedule']['first'][0]
            day2 = info['schedule']['second'][0]
            first_day = get_day_name(day1)
            second_day = get_day_name(day2)
            time1 = info['schedule']['first'][1]
            time2 = info['schedule']['second'][1]
            first_time = get_time(time1)
            second_time = get_time(time2)
            room1 = info['schedule']['first_day_room']
            room2 = info['schedule']['second_day_room']
            teacher_id = info['teacher']

            formatted = {
                "program": students_details[student_id]["program"],
                "year": students_details[student_id]["year"],
                "semester": students_details[student_id]["semester"],
                "block": students_details[student_id]["block"],
                'sched': []
            }

            if student_id in check_same_student:
                formatted["sched"].append({
                    "courseCode": course_code,
                    "courseDescription": courses_details[course_code]["description"],
                    "courseUnit": courses_details[course_code]["units"],
                    "day": f"{first_day}/{second_day}",
                    "time": f"{first_time}/{second_time}",
                    'room': f"{rooms_details[room1]['name']}/{rooms_details[room2]['name']}",
                    'instructor': teachers_details[teacher_id]["name"]
                })
            else:
                formatted["sched"] = [{
                    "courseCode": course_code,
                    "courseDescription": courses_details[course_code]["description"],
                    "courseUnit": courses_details[course_code]["units"],
                    "day": f"{first_day}/{second_day}",
                    "time": f"{first_time}/{second_time}",
                    'room': f"{rooms_details[room1]['name']}/{rooms_details[room2]['name']}",
                    'instructor': teachers_details[teacher_id]["name"]
                }]
                check_same_student.append(student_id)

            formatted_assignment["programs"].append(formatted)

        to_format_data.append(formatted_assignment)
        options_counter += 1  # Increment options_counter for the next assignment

    return to_format_data


def get_day_name(day):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Ensure that the day value is a string representing a number
    try:
        day_number = int(day)
        if 1 <= day_number <= 6:
            return days_of_week[day_number - 1]
        else:
            return "Invalid Day"
    except ValueError:
        return "Invalid Day"
    
def get_time(hour):
     start, end = hour
     s = convert_to_12_hour_format(start)
     e = convert_to_12_hour_format(end)
     time = f"{s}-{e}"
     return time

def convert_to_12_hour_format(hour):
    if hour == 12:
        return "12pm"  # Special case for 12pm
    elif hour > 12:
        return f"{hour - 12}pm"
    else:
        return f"{hour}am"
