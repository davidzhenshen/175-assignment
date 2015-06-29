

class student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.classes = []
    def add_grade(self, aclass):
        self.classes.append(aclass)
    def print_transcript(self):
        print(self.name + '-' + self.ID) 
        for i in self.classes:
            print(i)

    def converter(self, grade):
        if grade == 'A+':
            grade = 4.0
        if grade == 'A':
            grade = 4.0
        if grade == 'A-':
            grade = 3.7
        if grade == 'B+':
            grade = 3.3
        if grade == 'B':
            grade = 3.0
        if grade == 'B-':
            grade = 2.7
        if grade == 'C+':
            grade = 2.3
        if grade == 'C':
            grade = 2.0
        if grade == 'C-':
            grade = 1.7
        return grade    
    def comput_gpa(self):
        sum1 = 0
        for i in self.classes:
            newLists = i.split()
            sum1 = sum1 + int(self.converter(newLists[1]))
        print( sum1/len(self.classes))
            
        
        
        
        

            
        



afile = open('student.txt','r')
lines = afile.readlines()
#print(lines)
   
henry = student(lines[0],lines[1])
henry.add_grade(lines[2])
henry.add_grade(lines[3])
henry.print_transcript()
henry.comput_gpa()