class Subject:
    def __init__ (self,name,year,code,students):
        self._name = name
        self._year = year
        self._code = code
        self._students = students
    
    def __str__(self):
        return f"{self._name}, Year : {self._year}, Code: {self._code}, Students: {self._students}"

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
        
