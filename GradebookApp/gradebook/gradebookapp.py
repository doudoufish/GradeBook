from db import StudentRepository
from pathlib import Path
from school import Student
from typing import List
import os,sys
import csv


class GradebookApp:
    def __init__(self) -> None:
        studentsdb = StudentRepository()
        self.__student = studentsdb.getStudent()
        self.__numberOfWork = studentsdb.getNumberOfWork()
        self.__policy = studentsdb.getPolicy()
        self.__assiScores = studentsdb.getAssiScores()
        self.__testScores = studentsdb.getTestScores()
        self.__examScores = studentsdb.getExamScores()
        self.__finalScores = studentsdb.getFinalScores()

    def showTitle(self):
        print("This is the Grade Books")
        print()

    def showMenu(self):
        print("COMMAND MENU")
        print("S  - Set up for new semester. ")
        print("A - Add a student")
        print("P  - Record programming assignment score for all students")

        print("T  - Record Test score for all students")
        print("F  - Record F assignment score for all students")
        print("C  - Change grade for a particular student")
        print("G  - Calculate final score for all student")
        print("O  - output the grade as grades.out")
        print("Q - save all the student record and Quit")
        print()

    def setup(self):
        numberOfAssignment = int(input("please enter the number of assignment(range 0-6): "))
        print('The number of assignment set to : ', numberOfAssignment)
        numberOfTest = int(input("Please enter the number of tests.(range 0-4): "))
        print("The number of test set to: ", numberOfTest)
        numberOfExam = int(input("Please enter the number of Exam (Range 0-1): "))
        print("The number of exam set to: ",numberOfExam)
        
        numberOfWork = [numberOfAssignment,numberOfTest,numberOfExam]
        self.__numberOfWork = numberOfWork

        policy = [int(item) for item in input("Enter the percentage of the assignment,test,exam split with space(the sum of percentage should be 100) ").split()]
        if sum(policy) != 100:
            print("a valid number")
            policy = [int(item) for item in input("Enter the percentage of the assignment,test,exam split with space(the sum of percentage should be 100) ").split()]
        self.__policy = policy
        f_path  = './gradebook'
        f_name = "policy.txt"
        c_name = os.path.join(f_path,f_name)
        f = open(c_name,'w')
        f = open(c_name,"a")
        f.write("The school Policy:"+ "\n")
        f.write("In this semester: " + "\n" + "There are {} assignment".format(numberOfAssignment)+ "\n"
        + "There are {} test".format(numberOfTest)+ "\n"
        + "There are {} exam".format(numberOfExam)+ "\n"
        +"The percentage of the assignment is: {}".format(policy[0])+ "\n"
        +"The percentage of the Test is: {}".format(policy[1])+ "\n"
        +"The percentage of the Exam is: {}".format(policy[2]))

       
        

    def addStudent(self):
        id = input("Enter the student id (range 1-9999): ")
        name = input(
            "Enter the student last name and first name(most 20 characters): ")
        student = Student(id, name)
        self.__student.append(student)

    def recordAssignmentScore(self):
        if self.__numberOfWork[0] == 0:
            print("There is no assignment in this semester")
        else:
            numberOfWork = self.__numberOfWork[0]
            for x in range(numberOfWork):
                for student in self.__student:
                    print("Please enter the Score for assignment ",x,student.name, student.id, ': ',end='')
                    score = float(input()) 
                    self.__assiScores[student.name]=[0]* self.__numberOfWork[0]
                    self.__assiScores[student.name][x]=score

    def recordTestScore(self):
        if self.__numberOfWork[1] == 0:
            print("There is no Test in this semester")
        else:
            numberOfWork = self.__numberOfWork[1]
            for x in range(numberOfWork):
                for student in self.__student:
                    print("Please enter the Score for test ",x,student.name, student.id, ': ',end='')
                    score = float(input()) 
                    self.__testScores[student.name]=[0]* self.__numberOfWork[1]
                    self.__testScores[student.name][x]=score

    def recordExamScore(self):
        if self.__numberOfWork[2] == 0:
            print("There is no Exam in this semester")
        else:
            numberOfWork = self.__numberOfWork[2]
            for x in range(numberOfWork):
                for student in self.__student:
                    print("Please enter the Score for exam ",x,student.name, student.id, ': ',end='')
                    score = float(input()) 
                    self.__examScores[student.name]=[0]* self.__numberOfWork[2]
                    self.__examScores[student.name][x]=score
    def changeGrade(self):
        sid = int(input("Please enter the student id: "))
        newScore = float(input("Please enter the new Score: "))
        type = str(input("please enter the type of score change(P is assignment,T is a Test,F is a Final): "))
        if type == "P":
            number = int(input("Please enter the No of the assignment: "))
            for student in self.__student:
                if sid == student.id:                    
                    self.__assiScores[student.name][number-1]=newScore
                    
        elif type == "T":
            number = int(input("Please enter the No of the Test: "))
            for student in self.__student:
                if student.id == sid:
                    self.__testScores[student.name][number-1]=newScore
        elif type == "F":
            number = int(input("Please enter the No of the Final: "))
            for student in self.__student:
                if student.id == sid:
                    self.__examScores[student.name][number-1]=newScore
        else:
            print("Enter the wrong type")
        
    def finalScore(self):
        print(self.__assiScores)
        for student in self.__student:
            assigmentScore = sum(self.__assiScores[student.name])
            testScore = sum(self.__testScores[student.name])
            examScore = sum(self.__examScores[student.name])
            finalScores = assigmentScore * self.__policy[0]/100 + testScore * self.__policy[1]/100 + examScore * self.__policy[2]/100
            self.__finalScores[student.name] = finalScores

    def output(self):
        
        
     
        self.__student = sorted(sorted(self.__student, key=lambda x:x.id),key = lambda x:x.name, reverse=False)
        
        f_path  = './gradebook'
        f_name = "grades.out"
        c_name = os.path.join(f_path,f_name)
        f = open(c_name,'w')
        f = open(c_name,"a")
        for student in self.__student:
            f.write(student.name +','+ student.id + "\n")
            f.write("The all the record is: " + "\n")

            ffa = str(self.__assiScores[student.name]).replace("["," ").replace("]"," ")
            f.write("The all assignment score is: "+ ffa+ "\n")
            fft = str(self.__testScores[student.name]).replace("["," ").replace("]"," ")
            f.write("The all Test score is: "+ fft+ "\n")
            ffe = str(self.__examScores[student.name]).replace("["," ").replace("]"," ")
            f.write("The all exam score is: "+ ffe+ "\n")
            fff = str(self.__finalScores[student.name]).replace("["," ").replace("]"," ")
            f.write("The Final score is: "+ fff+ "\n")
 

         
         
          
    
    
    def quit(self):
        
        with open(Path(__file__).with_name("grades.csv"),'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            for student in self.__student:
                fs = ["student",student.id,student.name]
                writer.writerow(fs)        
                fa = ["assiScores",student.name,self.__assiScores[student.name]]
                writer.writerow(fa)        
                ft = ["testScores",student.name,self.__testScores[student.name]]
                writer.writerow(ft)     
                fe = ["examScores",student.name,self.__examScores[student.name]]
                writer.writerow(fe) 
                ff = ["finalScores",student.name,self.__finalScores[student.name]]
                writer.writerow(ff)



def main():
    app = GradebookApp()
    app.showTitle()
    
    # display Book objects

    while True:
        app.showMenu()
        command = input("Command: ")
        if command == "S":
            app.setup()
        elif command == "A":
            app.addStudent()
        elif command == "P":
            app.recordAssignmentScore()
        elif command == "T":
            app.recordTestScore()
        elif command == "F":
            app.recordExamScore()
        elif command == "C":
            app.changeGrade()
            print()
        elif command == "G":
            app.finalScore()
        elif command == "O":
            app.output()
        elif command == "Q":
            app.quit()
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
