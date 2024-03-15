
def formatting_data(result, students_details, courses_details, teachers_details, rooms_details):
    formatted_data = []
    
    for options_counter, sched in enumerate(result, start=1):
        check_same_student = {}
        programs = []

        for (student_id, course_code), info in sched.items():
            day1 = info['schedule']['first'][0]
            day2 = info['schedule']['second'][0]
            first_day = get_day_name(day1)
            second_day = get_day_name(day2)
            day_sched = f"{first_day}/{second_day}"
            time1 = info['schedule']['first'][1]
            time2 = info['schedule']['second'][1]
            first_time = get_time(time1)
            second_time = get_time(time2)
            time_sched = f"{first_time}/{second_time}"
            room1 = info['schedule']['first_day_room']
            room2 = info['schedule']['second_day_room']
            teacher_id = info['teacher']

            if student_id not in check_same_student:
                check_same_student[student_id] = {
                    "program": students_details[student_id]["program"],
                    "year": students_details[student_id]["year"],
                    "semester": students_details[student_id]["semester"],
                    "block": students_details[student_id]["block"],
                    "sched": []
                }
            
            student_schedule = {
                "courseCode": course_code,
                "courseDescription": courses_details[course_code]["description"],
                "courseUnit": courses_details[course_code]["units"],
                "day": day_sched,
                "time": time_sched,
                'room': f"{rooms_details[room1]['name']}/{rooms_details[room2]['name']}",
                'instructor': teachers_details[teacher_id]["name"]
            }
            check_same_student[student_id]["sched"].append(student_schedule)

        # Convert the dictionary into a list of programs
        for student_id, program_details in check_same_student.items():
            programs.append(program_details)

        option = f"option {options_counter}"
        formatted_data.append({"options": option, "programs": programs})

    return formatted_data


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
