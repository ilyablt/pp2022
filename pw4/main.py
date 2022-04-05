def Start_program():
    stulist = list()
    crslist = list()
    Students(stulist)
    Course(crslist)
    Marking(stulist, crslist)

    print("Displaying>>")
    for student in stulist:
        student.display()

    Sorting(stulist)
    print("Sorting>>")
    for student in stulist:
        student.display()

Start_program()