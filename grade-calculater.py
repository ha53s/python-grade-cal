

grades = {90: "A+", 86: "A", 82: "A-",
          78: "B+", 74: "B", 70: "B-",
          66: "C+", 62: "C", 58: "C-",
          54: "D+", 50: "D", 0: "F"}


# Function to calculate grade:


def get_grade():
    message = "Your grade is : \n "
    mark = int(input("Enter your mark: "))
    if 90 <= mark <= 100:
        print(message, grades[90])
    elif 86 <= mark < 90:
        print(message, grades[86])
    elif 82 <= mark < 86:
        print(message, grades[82])
    elif 78 <= mark < 82:
        print(message, grades[78])
    elif 74 <= mark < 78:
        print(message, grades[74])
    elif 70 <= mark < 74:
        print(message, grades[70])
    elif 66 <= mark < 70:
        print(message, grades[66])
    elif 62 <= mark < 66:
        print(message, grades[62])
    elif 58 <= mark < 62:
        print(message, grades[58])
    elif 54 <= mark < 58:
        print(message, grades[54])
    elif 50 <= mark < 54:
        print(message, grades[50])
    else:
        print(message, grades[0])


get_grade()


# Function to Calculate SGPA:


def calculate_sgpa():
    grade1 = input("Enter your first grade by letter: ")
    grade2 = input("Enter your second grade by letter: ")
    grade3 = input("Enter your third grade by letter: ")
    subjects = 0
    total_marks = 0
    if grade1 != 'None':
        subjects = subjects + 1
        total_marks = total_marks + points(grade1)

    if grade2 != 'None':
        subjects = subjects + 1
        total_marks = total_marks + points(grade2)

    if grade3 != 'None':
        subjects = subjects + 1
        total_marks = total_marks + points(grade3)
    if subjects == 0:
        return 0
    else:
        s_gpa = total_marks / subjects
        print("Your Semester GPA is :", s_gpa)


# Function that finds points to calculate the semester gpa :


def points(x):
    if x == "A+":
        return 4.00
    elif x == "A":
        return 4.00
    elif x == "A-":
        return 3.67
    elif x == "B+":
        return 3.33
    elif x == "B":
        return 3.00
    elif x == "B-":
        return 2.67
    elif x == "C+":
        return 2.33
    elif x == "C":
        return 2.00
    elif x == "C-":
        return 1.67
    elif x == "D+":
        return 1.33
    elif x == "D":
        return 1.00

    elif x == "F":
        return 0

calculate_sgpa()

# Function to Find cumulative marks :
def find_cumulative_marks(lst):
    if lst is not None:
        new_lst = []
        for student in lst:
            marks = sum(filter(None, student[2:]))
            new_stu = (student[0], student[1], marks)
            new_lst.append(new_stu)
        print("The Cumulative Marks:\n", new_lst)
    else:
        new_lst = []
        print("The Cumulative Marks :\n", new_lst)


results = [
    ('001234', 'Abdullah AlGhamdi', 64, 78.5, 89, 25, 99),
    ('001235', 'Hassan AlOtaibi', 14, 28.5, 83, 76),
    ('001236', 'Khalid AlShahrani', 87, None, 1.6)
]

find_cumulative_marks(results)
