# -----------------------Marks to Weightage Converter--------------------------

# Function to get maximum marks and weightage from user.
def getMinMax(type):
    List = list(map(eval, input(f"Please enter the Maximum weightage and Maximum marks for {type}: ").split()))
    if len(List) != 2:
        print("Please enter the valid input!")
        return getMinMax(type)
    return sorted(List, reverse=True)

# Getting Maximum Marks and Weightage for all Components.
SkillEndSem = getMinMax("SkillEndSem")
EndSem = getMinMax("EndSem")
LabEndSem = getMinMax("LabEndSem")
GlobalPlatforms = getMinMax("GlobalPlatforms")
SkillingContinuos = getMinMax("SkillingContinuos")
Alm = getMinMax("Alm")
HomeAssigment = getMinMax("HomeAssigment")
LabContinuousEvalutation = getMinMax("LabContinuousEvalutation")
Insem1= getMinMax("Insem1")
Insem2 = getMinMax("Insem2")
LabInSem = getMinMax("LabInSem")
SkillInSem = getMinMax("SkillInSem")



class InvalidMarksException(Exception):
    "Raised when invalid range is entered"
    def __init__(self,message="Entered data is not in a valid range"):
        self.message = message
        super().__init__(self.message)


# Function for getting input for Components that require only one input.
def getMarksInvidual(type,max_marks,max_weightage):
    try:
        marks = float(input(f"Please enter the {type} marks: (0 if not attempted, Max:{max_marks}): ").strip())
        if(marks>max_marks or marks<0): raise InvalidMarksException()
        marks = marks*(max_weightage/max_marks)
        return round(marks,3)
    except:
        print("Please enter the valid number:")
        return getMarksInvidual(type,max_marks,max_weightage)

# Function for getting input for Components that require multiple inputs.
def getMarksMultiple(type,maxMarks_per_co,maxWeightage_per_co,num_of_co,start=1):
    print(f"Please enter the {type} marks: (0 if not attempted, Max:{maxMarks_per_co} per CO!)")
    try:
        totalMarks = 0
        for i in range(start,num_of_co+1):
            marks = float(input(f"Co:{i} ").strip())
            if(marks>maxMarks_per_co or marks<0): raise InvalidMarksException()
            totalMarks+=marks*(maxWeightage_per_co/maxMarks_per_co)
        return round(totalMarks,3)
    except:
        print("Please enter the valid number:")
        return getMarksMultiple(type,maxMarks_per_co,maxWeightage_per_co,num_of_co,start)

# Class for Marks Analyser
class MarksAnalyzer:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.marks = []

    def get_marks(self):

        ## Skill-End-Exam
        x=getMarksInvidual("Skill-End-Exam",max(SkillEndSem),min(SkillEndSem))
        self.marks.append(x)

        ## Lab-End-Exam
        x=getMarksInvidual("Lab-End-Exam",max(LabEndSem),min(LabEndSem))
        self.marks.append(x)

        ## End-Exam
        x=getMarksMultiple("End-Exam",max(EndSem)/4,min(EndSem)/4,4)
        self.marks.append(x)


        ## Global Platforms
        x=getMarksInvidual("Global-Platform",max(GlobalPlatforms),min(GlobalPlatforms))
        self.marks.append(x)

        ## Skilling-Continuous-Evaluation
        x=getMarksInvidual("Skilling-Continuous-Evalutation",max(SkillingContinuos),min(SkillingContinuos))
        self.marks.append(x)

        ## ALM
        x=getMarksMultiple("ALM",max(Alm)/4,min(Alm)/4,4)
        self.marks.append(x)

        ## Home-Assignment
        x=getMarksMultiple("Home-Assignment",max(HomeAssigment)/4,min(HomeAssigment)/4,4)
        self.marks.append(x)

        ## Continuous-Evaluation-Lab-Exercise
        x=getMarksInvidual("Continuous-Evaluation-Lab-Exercise",max(LabContinuousEvalutation),min(LabContinuousEvalutation))
        self.marks.append(x)

        ## Semister-InExam1
        x=getMarksMultiple("InSem-1",max(Insem1)/2,min(Insem1)/2,2)
        self.marks.append(x)

        ## Semister-InExam2
        x=getMarksMultiple("InSem-2",max(Insem2)/2,min(Insem2)/2,4,3)
        self.marks.append(x)

        ## Lab In-Semsister
        x=getMarksInvidual("Lab-InSem",max(LabInSem),min(LabInSem))
        self.marks.append(x)

        ## Skill In-Semsister
        x=getMarksInvidual("Skill-InSem",max(SkillInSem),min(SkillInSem))
        self.marks.append(x)


    
    def EndSemesterSummativeMarks(self):
        print("----Marks Analysis----")
        print("Name=",self.name)
        print("Roll No=",self.rollNo)
        print("-----------------------")
        print("Skill End-Sem Weightage:",self.marks[0])
        print("Lab End-Sem: Weightage:",self.marks[1])
        print("End-Sem Weightage:",self.marks[2])
        totalMarks = sum(mark for mark in self.marks[:3] if mark is not None)
        print("Total marks in End-Semester-Summative Evaluation:",totalMarks)

    def InSemesterFormativeMarks(self):
        print("-----------------------")
        print("Global Platform Weightage:",self.marks[3])
        print("Skilling Continuous Evaluation Weightage:",self.marks[4])
        print("ALM Weightage:",self.marks[5])
        print("Home-Assignment Weightage:",self.marks[6])
        print("Continuous Evalutation Lab Weightage:",self.marks[7])

        totalMarks = sum(mark for mark in self.marks[3:8] if mark is not None)
        print("Total marks in In-Semester-Formative Evaluation:",totalMarks)

    def InSemesterSummativeMarks(self):
        print("-----------------------")
        print("In-Sem 1 Weightage:",self.marks[8])
        print("In-Sem 2 Weightage:",self.marks[9])
        print("Lab In-Sem Weightage:",self.marks[10])
        print("Skill In-Sem Weightage:",self.marks[11])

        totalMarks = sum(mark for mark in self.marks[8:] if mark is not None)
        print("Total marks in In-Semester-Summative Evaluation:",totalMarks)

    def printTotalMarks(self):
        self.EndSemesterSummativeMarks()
        self.InSemesterFormativeMarks()
        self.InSemesterSummativeMarks()
        print("---------------------------")
        totalMarks = sum(mark for mark in self.marks if mark is not None)
        print(f"Total Marks = {totalMarks}/100")


if __name__ == '__main__':
    student = MarksAnalyzer("Sweshik",2310080053)
    student.get_marks()
    student.printTotalMarks()
