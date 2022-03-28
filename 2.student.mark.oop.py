class Student:
    def __init__(stu, test, sid, name, dob):
        stu.__sid = sid
        stu.__name = name
        stu.__dob = dob
        stu_info = {'ID' : sid, 'Name' : name, 'DOB' : dob}
        test.students.append(stu_info)

    def get_sid(stu):
        return stu.__sid

    def get_name(stu):
        return stu.__name

    def get_dob(stu):
        return stu.__dob

class Course:
    def __init__(crs, test, cid, name):
        crs.__cid = cid
        crs.__name = name
        crs_info = {'id' : cid, 'name' : name}
        test.courses.append(crs_info)

    def get_cid(crs):
        return crs.__cid

    def get_name(crs):
        return crs.__name

class Mark:
    def __init__(obj, test, sid, cid, mark):
        obj.__sid = sid
        obj.__cid = cid
        obj.__mark = mark
        mark_Info = {'Student id' : sid, 'Course id' : cid, 'mark' : mark}
        test.marks.append(mark_Info)

    def get_sid(obj):
        return obj.__sid

    def get_cid(obj):
        return obj.__cid

    def get_mark(obj):
        return obj.__mark

class Test:
    students = []
    courses = []
    marks = []
    
    def listStudent (x) :
        print(students)

    def listCourse (x) :
        print(courses)
    
    def listMark (x):
        print(marks)
    
    def start (x):  
        student_no = int(input('Enter the number of students : '))
        for i in range (student_no) :
            sid = input('\nEnter student ID : ')
            sname = input('Enter student name: ')
            sdob = input('Enter student DOB: ')
            temp_Student = Student(x, sid, sname, sdob)
            
        course_no = int(input('****************\nEnter the number of courses: '))
        for y in range (course_no):
            cid = input('\nEnter the course ID: ')
            course_Name = input('Input the name of the course: ')
            temp_Course = Course(x, cid, course_Name)
        
        count = 0    
        while count == 0:
            sid1 = int(input('****************\nEnter student ID to mark: '))
            cid1 = int(input('Enter course ID: '))
            mark = int(input('Enter mark: '))
            Mark(x, sid1, cid1, mark)
            print('Do you want to continue ? Press 0 for Yes, press 1 for No.')
            count  = int(input())

if __name__ == '__main__':
    program = Test()
    program.start()