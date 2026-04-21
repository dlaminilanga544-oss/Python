grade = int(input("Enter your marks: "))

def get_grade(grade):
    if grade >= 90 and grade <= 100:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 60 and grade <= 60:
        return "D"
    elif grade >= 50 and grade <= 50:
        return "E"
    elif grade >= 40 and grade <= 40:
        return "F"
    else:
        return "U"
    
print (str(get_grade(grade)))