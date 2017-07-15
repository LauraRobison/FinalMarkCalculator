'''Calculate the mark needed in final to get the desired grade'''

FILE_NAME = "marks.csv"


def total_lines():
    '''Returns the number of lines in the file

    Returns:
        An int telling the number of lines in the file

    Raises:
        FileNotFoundError: If the file is not in the same directory as the code
    '''
    fname = open(FILE_NAME, 'r')
    lines = fname.readlines()
    fname.close()
    return len(lines)


def calculate_final():
    '''Calculates the percent grade required in final to get the desired grade

    The file has to be of csv format, all fields are int and the fields has
    to ordered:
        First line: name of course, desired_grade
        All other lines: [name of assigment, achieved mark,
            total mark, worth of assignment in course]

    Returns:
        An int telling the percent grade needed in final to get desired grade

    Raises:
        FileNotFoundError: If the file is not in the same directory as the code
    '''
    percent_grades = []
    final_location = total_lines() - 1

    with open(FILE_NAME, 'r') as fname:
        for line, info in enumerate(fname):
            info = info.strip().split(',')
            if line is 0:
                desired_grade = int(info[1])
            elif line is final_location:
                required_percent = desired_grade - sum(percent_grades)
                return int((required_percent / int(info[3])) * 100)
            else:
                # info[1] is achieved mark in assignment, info[2] is total
                # mark of assignment, info[3] is worth of assignment in course
                percent_grades.append(
                    (int(info[1]) / int(info[2])) * int(info[3]))


def main():
    '''Displays the percent required in final to get the desired grade. Also
    displays a message telling if the desired grade is achievable or not.
    '''
    mark_required = calculate_final()
    print(('You need {0}% in your final').format(mark_required))

    if mark_required > 100:
        print("NOT POSSIBLE")
    else:
        print("You can do it cookie")


main()
