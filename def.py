#1
def finance_student(name,income,expenses):
    balance = lambda income,expenses: income - expenses 
    finance = {
        'name': name,
        'income': income,
        'expenses': expenses,
        'balance': balance(income,expenses)
    }    
    return finance
name = input('Enter your name:')
income = float(input('Enter your income'))
expenses = float(input('Enter your expenses'))
print(finance_student(name,income,expenses))

#2     
def bmi(height, weight):
    bmi = weight / (height / 100) ** 2
    if bmi <= 18.5:  
        result = 'You are underweight' 
    elif bmi <= 24.9:  
        result = 'Weight is normal' 
    elif bmi <= 29.9:  
        result = 'You am overweight'
    else:  
        result = 'Urgently on a diet:)'
    return result    
height = float(input('Enter height in cm:'))  
weight = float(input('Enter weight in kg:'))
print(bmi(height, weight))
#3
def gpa():
    gpa
list['subject','score']    
for x in range(0,2):    
    subject = input('Enter name subject')
    score = int(input("Enter your exam score: "))
    
    
    def grade(score):


        grade = ""
        if score < 60:
            grade = "F"
        elif score < 70:
            grade = "D"
        elif score < 80:
                grade = "C"
        elif score < 90:
            grade = "B"
        elif score < 100:
            grade = "A"
            

        return f"Your grade is {grade}."


    print(grade(score))


gpa()      