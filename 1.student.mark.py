#Input number of students in a class
def student_num():
    ns = int(input("Enter the number of the students in the class: "))
    return ns

#Input student information: id, name, DoB
def student_info():
    stulist=[]
    for i in range(0,ns,1):
        sid = input("Enter student ID: ")
        sname = input("Enter student name: ")
        dob = input("Enter student DOB: ")
        print("___________________")
        s =("{ID: " + sid + ", Name: " + sname + ", DOB: " + dob + "}")
        stulist.append(s)
    print("Student list:")
    print(stulist)
    print("**************************************************")

#Input number of courses
def course_num():
    nc = int(input("Enter the number of the courses: "))
    return nc

#Input course information: id, name
def course_info():
    crslist = []
    for i in range(0,nc,1):
        cid = input("Enter course ID: ")
        cname = input("Enter course name: ")
        c = ("{ID: " + cid  + ", Name: " + cname + "}")
        crslist.append(c)
    print("Courses list:")
    print(crslist)
    print("**************************************************")

#Select a course, input marks for student in this course
def input_marks():
    select_course = input("Select a course ID: ")
	  for i in range(len(course)):
		    if course[i].get("ID") == select_course:
			      cid = course[i].get("name")
			      m = {"Course": cid, "Students and marks": []}
			      print("Course name: " + course[i].get("name") + "\n")
			      for j in range(len(students)):
				        mark = float(input("\tEnter " + students[j].get("Name") + "'s mark "))
				        sid = students[j].get("Name")
				        m["Students and marks"].append((sid, mark))
			      return m
#List courses
def list_course():
    print(courseList)

#List students
def list_students():
    print(studentList)

#Show student marks for a given course
def list_course_marks():
    print(mark)

student_num()
student_info()
course_num()
course_info()
input_marks()
list_course()
list_students()
list_course_marks()