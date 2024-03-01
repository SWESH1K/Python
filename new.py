import math

def getMarksInvidual(type,max_marks,max_weightage):
    print(f"Please enter the {type} marks: (0 if not attempted, Max:{max_marks})")
    try:
        marks = int(input())
        marks = marks*(max_weightage/max_marks)
        return marks
    except Exception as error:
        print("Please enter the valid number:")
        print(error)
        exit()

def getMarksMultiple(type,maxMarks_per_co,maxWeightage_per_co,num_of_co,start=1):
    print(f"Please enter the {type} marks: (0 if not attempted, Max:{maxMarks_per_co} per CO!)")
    try:
        totalMarks = 0
        for i in range(start,num_of_co+1):
            marks = eval(input(f"Co:{i} "))
            totalMarks+=marks*(maxWeightage_per_co/maxMarks_per_co)
        return totalMarks
    except:
        print("Please enter the valid number:")
        exit()

class MarksAnalyzer:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.marks = []

    def get_marks(self):

        ## Skill-End-Exam
        x=getMarksInvidual("Skill-End-Exam",50,8)
        self.marks.append(x)

        ## Lab-End-Exam
        x=getMarksInvidual("Lab-End-Exam",50,8)
        self.marks.append(x)
        
        ## End-Exam
        x=getMarksMultiple("End-Exam",25,6,4)
        self.marks.append(x)


        ## Global Platforms
        x=getMarksInvidual("Global-Platform",50,2)
        self.marks.append(x)

        ## Skilling-Continuous-Evaluation
        x=getMarksInvidual("Skilling-Continuous-Evalutation",50,5)
        self.marks.append(x)

        ## ALM
        x=getMarksMultiple("ALM",12.5,2,4)
        self.marks.append(x)

        ## Home-Assignment
        x=getMarksMultiple("Home-Assignment",12.5,1,4)
        self.marks.append(x)

        ## Continuous-Evaluation-Lab-Exercise
        x=getMarksInvidual("Continuous-Evaluation-Lab-Exercise",50,5)
        self.marks.append(x)
        
    def printEndSemesterSummativeMarks(self):
        print("----Marks Analysis----")
        print("Name=",self.name)
        print("Roll No=",self.rollNo)
        print("-----------------------")
        print("Skill End-Sem Weightage:",self.marks[0])
        print("Lab End-Sem: Weightage:",self.marks[1])
        print("End-Sem Weightage:",self.marks[2])
        totalMarks = self.marks[0]+self.marks[1]+self.marks[2]
        print("Total marks in End-Semester-Summative Evaluation:",totalMarks)

    def InSemesterFormativeMarks(self):
        print("-----------------------")
        print("Global Platform Weightage:",self.marks[3])
        print("Skilling Continuous Evaluation Weightage:",self.marks[4])
        print("ALM Weightage:",self.marks[5])
        print("Home-Assignment Weightage:",self.marks[6])
        print("Continuous Evalutation Lab Weightage:",self.marks[7])

        totalMarks = self.marks[3]+self.marks[4]+self.marks[5]+self.marks[6]+self.marks[7]
        print("Total marks in End-Semester-Summative Evaluation:",totalMarks)

    def printTotalMarks(self):
        self.printEndSemesterSummativeMarks()
        self.InSemesterFormativeMarks()

if __name__ == '__main__':
    student = MarksAnalyzer("Sweshik",2310080053)
    student.get_marks()
    student.printTotalMarks()