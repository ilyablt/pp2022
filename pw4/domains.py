stulist = list()
crslist = list()

class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.listCourseMark = list()
    
    def setName(self,name):
        name = self.name

    def getName(self):
         return self.name

    def setID(self):
        self.id = id

    def getID(self):
        return self.id

    def setDob(self,dob):
        self.dob = dob

    def setCoursemark (self, course, mark):
        courseMark = {"course": course, "mark": mark}        
        self.listCoursemark.append(courseMark)
    
    def get_avgmark(self):
        sumMark = 0;
        for courseMark in self.listCourseMark:
            sumMark += courseMark["mark"]

        average = sumMark/len(self.listCourseMark)
        return math.floor(average*10)/10

    def display(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("DOB: ", self.dob)
        print("Mark list: ", self.listCourseMark)
        print("GPA: ", self.get_avgmark())
        print("\n")

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def setName(self):
        name = self.name

    def getName(self):
        return self.name

    def setID(self):
        self.id = id

    def getID(self):
        return self.id         

    def display(self):
        print("Course: ", self.name)
        print("Course ID: ", self.id)  
        print("\n")
