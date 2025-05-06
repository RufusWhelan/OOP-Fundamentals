from Subjects import *
import random

allsubjects = SubjectList()


def add(subjectName):
    addedSubject = Subject(subjectName, random.randint(7, 12), random.randint(1000,1999), random.randint(20,35))
    allsubjects.addSubject(addedSubject)
    print(f"added: {addedSubject}")

def search(subjectName):
    enteredclass = allsubjects.findSubject(subjectName)
    print(enteredclass)

def view(): 
    allsubjects.displaySubjects()


choice = 1
while choice != 4:
    try:
        choice = int(input("To add a subject type 1, to view added subjects type 2, to view all subject details type 3, type 4 to quit the program: "))
        if choice == 1:
            subject = input("Input subject you want to add to your subjects: ")
            add(subject)
        elif choice == 2:
            subject = input("Input subject you want to view in your clas list: ")
            search(subject)
        elif choice == 3:
            view()
        elif choice == 4:
            print("goodbye")
    
    except:
        print("please enter an integer.")