class Calc():
	def __init__(self, studentName):
		self.__name = studentName

	# Method to get studentName
	@property
	def name(self):
		return self.__name

	# Method to display welcome message
	def displayMessage(self):	
		print("\nWelcome to CalcCGPA,", self.__name)
		print("Copyright iCorp")
	
	# Method to perform CGPA calculation
	def calcCGPA(self):
		numOfCourses = int(input("\nHow many courses did you register? "))
		# Initialization phase 
		gradeCounter = 1
		totalUnit = 0
		wgpTotal = 0
		# Processing phase
		for gradeCounter in range(numOfCourses):
			grade = int(input("\nEnter grade: "))
			courseUnit = int(input("Enter course unit: "))
			if grade >= 70:
				gp = 7
			elif grade >= 65:
				gp = 6
			elif grade >= 60:
				gp = 5
			elif grade >= 55:
				gp = 4
			elif grade >= 50:
				gp = 3
			elif grade >= 45:
				gp = 2
			elif grade >= 40:
				gp = 1
			else:
				gp = 0
			wgp = (gp * courseUnit)
			wgpTotal += wgp
			totalUnit += courseUnit
			print("Grade Point:", gp)
			print("Weighted Grade Point:", (gp * courseUnit))
			gradeCounter = gradeCounter + 1
			
		# Termination phase
		cgpa = (wgpTotal / totalUnit)
		
		# Display number of courses and total
		print("\nYou registered", numOfCourses, "courses")
		print("Total Weighted Grade Point (WGP) is", wgpTotal)
		print("Dividing", wgpTotal, "by", totalUnit, "gives your CGPA")
		print("Your CGPA is %.1f" % cgpa)
		# Goodbye message
		print("\nThanks for using this app,", self.__name)