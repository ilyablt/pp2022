import domains
import math

def Students(stulist):
    stunum = int(input("Enter the number of students : "))

    for i in range(0, stunum):
        id = input("\nEnter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DOB:  ")

        stulist.append(Student(id, name, dob))

def Course(crslist):
    crsnum = int(input('****************\nEnter the number of courses: '))
    for i in range(0, crsnum):
        id = int(input("\nEnter course ID: "))
        name = input("Enter course name: ")
        crslist.append(Course)

def Marking(stulist, crslist):
    chosen_course = int(input("****************\nEnter the course ID to mark: "))
    for i in range(len(crslist)):
        x = int(crslist[i].getID)
        if chosen_course == x:
            for s in stulist:
                mark = float(input("Enter mark of student:"+ s.getName() + " for course " + c.getName() + ": "))
                s.setCourseMark(c.getName(), math.floor(mark*10)/10)

def Sorting(stulist):
    stulist.sort(key = lambda student: student.get_avgmark(), reverse = False)