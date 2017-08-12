from cgpa import Calc

studentName = input("What's your name? ")
student = Calc(studentName)
student.displayMessage()
student.calcCGPA()