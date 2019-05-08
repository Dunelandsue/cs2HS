"""Student"""
#Ethan Wodrich
def add_students():
    students.append(Student("Shaggy","1234567",11,2.0,"C"))
    students.append(Student("Fred","0000000",5,5.0,"A"))
    students.append(Student("Velma","1357911",9,5.0,"D"))
    students.append(Student("Scooby","0246810",12,1.0,"B"))

class Student(object):
    num_studs = 0

    def __init__(self,name,stud_id,grade,gpa,lunch):
        self.name = name
        self.__stud_id = stud_id
        self.grade = grade
        self.__gpa = gpa
        self.lunch = lunch
        Student.num_studs += 1

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def new_gpa(self,gpa):
        self.__gpa = gpa

    def __str__(self):
        string = "\n__Student__\nname: {}\tstud_id: {}\tgrade: {}\ngpa: {}\tlunch: {}\n".format(
            self.name,self.__stud_id,self.grade,self.__gpa,self.lunch)
        return string

    def year_end(self):
        print(self.name,self.grade,end=" ")
        self.grade += 1
        print("new",self.grade)

def main():
    global students
    students = []
    add_students()

    print(students[0])
    print(students[0].name)
    for i in students:
        print(i)
    print("The total number of students is", Student.num_studs)
    students[3].new_gpa = 3.9
    print(students[3])
    for i in students:
        i.year_end()
    for i in students:
        print(i)
    for student in students:
        if student.grade == 13:
            students.remove(student)
            del student
    print("Removed students")
    for i in students:
        print(i)
    print("The total number of students after delete is", Student.num_studs)

main()
input("\n\npress enter")
