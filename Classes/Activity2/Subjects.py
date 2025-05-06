class Subject:
    def __init__ (self,name,year,code,students):
        self.name = name
        self.year = year
        self.code = code
        self.students = students
    
    def __str__(self):
        return f"{self.name}, Year : {self.year}, Code: {self.code}, Students: {self.students}"

class SubjectList:
    def __init__(self):
        self.subjects = []
    
    def addSubject(self, subject):
        self.subjects.append(subject)

    def findSubject(self, name):
        for subject in self.subjects:
            if subject.name == name: 
                return subject
        return "invalid subject"
    
    def displaySubjects(self):
        for subject in self.subjects: 
            print(subject)
        return None
        
