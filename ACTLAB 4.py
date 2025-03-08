def assign_grade(score):
    if score < 0 or score > 100:
        print("invalid score, please enter a value between 0 and 100")
        return
    
    elif score >= 90:
        print("grade is A")
    elif score >= 80:
        print("grade is B")
    elif score >= 70:
        print("grade is C")
    elif score >= 60:
        print("grade is D")
    else:
        print("grade is F")
        
while True:
    score = int(input("enter a score: "))
    assign_grade(score)