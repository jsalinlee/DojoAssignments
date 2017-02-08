import random
def grader(numStudents):
    grade = ""
    for count in range(numStudents):
        score = random.random()*100 + 1
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print "Score: " + str(int(score)) + ": You got a(n) " + grade
grader(10)
