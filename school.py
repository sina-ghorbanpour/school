import json
level="root"
class Course:
    id:int=0
    name:str=""
    units:int=0
    score:int=0
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
    def __eq__(self,other):
        return self.id==other.id
#----------------------------------------------------------
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
    def __eq__(self,other):
        return self.id==other.id
#----------------------------------------------------------
class Teacher:
    id:int=0
    name:str=""
    family:str=""
    grade:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family,grade):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
    def __eq__(self,other):
        return self.id==other.id
#----------------------------------------------------------
class Classroom:
    id:int=0
    name:str=""
    course:Course=None
    teacher:Teacher=None
    students:list[Student]=[]
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __eq__(self,other):
        return self.id==other.id
#----------------------------------------------------------
class School:
    name:str=""
    courses:list[Course]=[]
    teachers:list[Teacher]=[]
    students:list[Student]=[]
    selected_student:Student=None
    selected_teacher:Teacher=None
    def __init__(self,name):
        self.name=name
#===========================================================
    def add_student(self,student):
        if student in self.students:
            print("already exist!")
        else:
            self.students.append(student)
    def delete_student(self,id):
        student=Student(id,"","")
        if student in self.students:
            self.students.remove(student)
        else:
            print("doesnt exist!")
#===========================================================
    def add_teacher(self,teacher):
        if teacher in self.teachers:
            print("already exist!")
        else:
            self.teachers.append(teacher)
    def delete_teacher(self,id):
        t1=Teacher(id,"","","")
        if t1 in sc1.teachers:
            sc1.teachers.remove(t1)
        else:
            print("doesnt exist!")
#===========================================================
    def load_data(self):
        f1=open("data.json","rt")
        l=f1.read()
        f1.close()
        data=json.loads(l)
        for crs in data["courses"]:
            self.courses.append(Course(crs["id"],crs["name"],crs["units"]))
        for std in data["students"]:
            self.students.append(Student(std["id"],std["name"],std["family"]))
        for tch in data["teachers"]:
            self.teachers.append(Teacher(tch["id"],tch["name"],tch["family"],tch["grade"]))
#===========================================================
    def save_data(self):
        students=[]
        teachers=[]
        courses=[]
        for crs in self.courses:
            courses.append({"id":crs.id,"name":crs.name,"units":crs.units})
        for std in self.students:
            students.append({"id":std.id,"name":std.name,"family":std.family})
        for tch in self.teachers:
            teachers.append({"id":tch.id,"name":tch.name,"family":tch.family,"grade":tch.grade})
        data={"courses":courses,"students":students,"teachers":teachers}
        f1=open("data.json","wt")
        s=json.dumps(data)
        f1.write(s)
        f1.close()
#===========================================================
sc1=School("yasa")
sc1.load_data()
while True:
    if level == "root":
        print("1.students")
        print("2.teachers")
        print("3.courses")
        print("4.classrooms")
        print("5.save")
        print("0.exit")
        cmd=int(input(">>:"))
        if cmd == 1:
            level="students"
        elif cmd == 2:
            level="teacher"
        elif cmd == 3:
            level="courses"
        elif cmd == 4:
            level="classrooms"
        elif cmd == 5:
            level="save"
        elif cmd == 0:
            break
#STUDENT
    elif level == "students":
        print("1.show students")
        print("2.add student")
        print("3.edit student")
        print("4.delete studnet")
        print("5.select student")
        print("0.back")
        cmd=int(input(">>:"))
        #Show
        if cmd == 1:
            for student in sc1.students:
                    print(student.id,student.name,student.family)
        #Add
        elif cmd == 2:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            s1=Student(id,name,family)
            sc1.add_student(s1)
        #Edit
        elif cmd == 3:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            s1=Student(id,"","")
            if s1 in sc1.students:
                result=sc1.students.index(s1)
                sc1.students[result].name=name
                sc1.students[result].family=family
            else:
                print("doesnt exist!")
        #Delete
        elif cmd == 4:
            id=int(input("id:"))
            sc1.delete_student(id)
        #Select
        elif cmd == 5:
            level = "select student"
        #Back
        elif cmd == 0:
            level="root"
#TEACHER
    elif level == "teacher":
        print("1.show teachers")
        print("2.add teacher")
        print("3.edit teacher")
        print("4.delete teacher")
        print("5.select teacher")
        print("0.back")
        cmd=int(input(">>:"))
        #Show
        if cmd == 1:
            for teacher in sc1.teachers:
                    print(teacher.id,teacher.name,teacher.family,teacher.grade)
        #Add
        elif cmd == 2:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            grade=input("grade:")
            t1=Teacher(id,name,family,grade)
            sc1.add_teacher(t1)
        #Edit
        elif cmd == 3:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            grade=input("grade:")
            t1=Teacher(id,"","","")
            if t1 in sc1.teachers:
                result=sc1.teachers.index(t1)
                sc1.teachers[result].name=name
                sc1.teachers[result].family=family
                sc1.teachers[result].grade=grade
            else:
                print("doesnt exist!")
        #Delete
        elif cmd == 4:
            id=int(input("id:"))
            sc1.delete_student(id)
        #Select
        elif cmd == 5:
            level="select teacher"
        #Back
        elif cmd == 0:
            level="root"
#COURSE
    elif level == "courses":
        print("1.show courses")
        print("2.add course")
        print("3.edit course")
        print("4.delete course")
        print("0.back")
        cmd=int(input(">>:"))
        #Show
        if cmd == 1:
            for course in sc1.courses:
                    print(course.id,course.name,course.units)
        #Add
        elif cmd == 2:
            id=int(input("id:"))
            name=input("name:")
            unit=int(input("unit:"))
            c1=Course(id,name,unit)
            if c1 in sc1.courses:
                print("already exist!")
            else:
                sc1.courses.append(c1)
        #edit
        elif cmd == 3:
            id=int(input("id:"))
            name=input("name:")
            units=int(input("unit:"))
            c1=Course(id,"","")
            if c1 in sc1.courses:
                result=sc1.courses.index(c1)
                sc1.courses[result].name=name
                sc1.courses[result].units=units
        #Delete
        elif cmd == 4:
            id=int(input("id:"))
            s1=Course(id,name="",units=0)
            if c1 in sc1.courses:
                sc1.courses.remove(c1)
            else:
                print("doesnt exist!")
        elif cmd == 0:
            level="root"
    elif level == "classrooms":
        print("1.show classrooms")
        print("2.add classroom")
        print("3.edit classroom")
        print("4.delete classroom")
        print("5.select classroom")
        print("0.back")
        cmd=int(input(">>:"))
#CLASSROOM
        if cmd == 1:
            pass
        elif cmd == 2:
            pass
        elif cmd == 3:
            pass
        elif cmd == 4:
            pass
        elif cmd == 5:
            pass
        elif cmd == 0:
            level="root"
#Save
    elif level == "save":
        sc1.save_data()
        level="root"
#Select student
    if level == "select student":
        for student in sc1.students:
            print(student.id,student.name,student.family)
        selected_std_id=int(input("enter id:"))
        selected_std_id=Student(selected_std_id,None,None)
        if selected_std_id in sc1.students:
            k=sc1.students.index(selected_std_id)
            sc1.selected_student=sc1.students[k]
            print("1.show info")
            print("2.add course")
            print("3.delete courses")
            print("4.set scores")
            print("0.back")
            select_cmd=int(input(">>:"))
        else:
            print("The current id doesnt exist!")
        level="students"
        if select_cmd==1:
            print(sc1.selected_student.id)
            print(sc1.selected_student.name)
            print(sc1.selected_student.family)
            for course in sc1.selected_student.courses:
                print(course.id,course.name)
        elif select_cmd==2:
            for course in sc1.courses:
                print(course.id,course.name,course.units)
            id=int(input("id:"))
            id=Course(id,None,None)
            if id in sc1.courses:
                k=sc1.courses.index(id)
                sc1.selected_student.courses.append(sc1.courses[k])
                print("its done")
            else:
                print("The current id doesnt exist!")
        elif select_cmd==3:
            for course in sc1.selected_student.courses:
                print(course.id,course.name)
            id=int(input("id:"))
            id=Course(id,"",0)
            if id in sc1.selected_student.courses:
                sc1.selected_student.courses.remove(id)
        elif select_cmd==4:
            pass
        elif select_cmd==0:
            level="students"
#Select teacher
    if level == "select teacher":
        for teacher in sc1.teacher:
            print(teacher.id,teacher.name,teacher.family,teacher.grade)
        selected_tch_id=int(input("enter id:"))
        selected_tch_id=Teacher(id,"","","")
        if selected_tch_id in sc1.teachers:
            k=sc1.teachers.index(selected_tch_id)
            sc1.selected_teacher=sc1.teachers[k]
        else:
            print("1.show info")
            print("2.add course")
            print("3.delete courses")
            print("0.back")
        select_cmd=int(input(">>:"))
        if select_cmd==1:
            pass
        elif select_cmd==2:
            pass
        elif select_cmd==3:
            pass
        elif select_cmd==0:
            level="teacher"
