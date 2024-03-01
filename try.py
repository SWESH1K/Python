def Summative(): 
    try:
        skill = float(input("Enter marks scored in End Sem Skill Exam out of 50"))
        while True:
            if (skill > 50):
                print("Please enter valid marks ")
            else:
                skill_w = (8 / 50) * skill
                break
        end = float(input("Enter marks scored in End Sem Exam out of 100"))
        while True:
            if (end > 100):
                print("Please enter valid marks ")
            else:
                end_w = (24 / 100) * skill
                break
        lab = float(input("Enter marks scored in Lab End Sem Skill Exam out of 50"))
        while True:
            if (lab > 50):
                print("Please enter valid marks ")
            else:
                lab_w = (8 / 50) * skill
                break
        summ_w = skill_w + end_w + lab_w
        return summ_w
    except:
        print("Please try again")

def Formative(): 
    try:
        rate = float(input("Enter marks scored for Rating on Global Platforms out of 50"))
        while True:
            if (rate > 50):
                print("Please enter valid marks ")
            else:
                rate_w = (2 / 50) * rate
                break
        cont = float(input("Enter marks scored in Skilling Continouous Evaluation out of 50"))
        while True:
            if (cont > 50):
                print("Please enter valid marks ")
            else:
                cont_w = (5 / 50) * cont
                break
        alm = float(input("Enter marks scored in Lab End Sem Skill Exam out of 50"))
        while True:
            if (alm > 50):
                print("Please enter valid marks ")
            else:
                alm_w = (8 / 50) * alm
                break
        home = float(input("Enter marks scored in Lab End Sem Skill Exam out of 50"))
        while True:
            if (home > 50):
                print("Please enter valid marks ")
            else:
                home_w = (4 / 50) * home
                break
        labb = float(input("Enter marks scored in Continuous Lab Evaluation out of 50"))
        while True:
            if (labb > 50):
                print("Please enter valid marks")
            else:
                labb_w = (5/ 50) * labb
                break
        form_w = labb_w + alm_w + home_w + cont_w + rate_w
        return form_w
    except:
        print("Please try again")

def SemSummative():
    try:
        sem_1 = float(input("Enter marks scored in In-Sem 1 out of 50"))
        while True:
                if(sem_1 > 50):
                    print("Please enter valid marks:")
                else:
                    sem_1_w = (12 / 50) * sem_1
                    break
        sem_2 = float(input("Enter marks scored in In-Sem 2 out of 50"))
        while True:
            if(sem_2 >50):
                 print("enter valid marks:")
            else:
                    sem_2_w = (12 / 50) * sem_2
                    break
        labsem = float(input("Enter marks scored in Lab In Sem Exam out of 50"))
        while True:
            if (labsem > 50):
                print("Please enter valid marks ")
            else:
                labsem_w = (6 / 50) * labsem
                break
       
        skillsem = float(input("Enter marks scored in Skill In-Sem Exam out of 50"))
        while True:
            if(skillsem >50):
                print("enter valid marks:")
            else:
                    skillsem_w = (6 / 50) * skillsem
                    break
        sem = sem_1_w + sem_2_w + skillsem_w + labsem_w
        return sem
    except:
        print("Please try again")


one = Summative()
two = Formative()
thr = SemSummative()

print("End Semester Summative Evaluation Total out of 40% =", one)
print("In Semester Formative Evaluation Total out of 24% =", two)
print("In Semester Summative Evaluation Total out of 36% =", thr)
print("Total Score =", one + two + thr)