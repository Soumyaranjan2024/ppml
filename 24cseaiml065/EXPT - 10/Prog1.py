#SINGLE INHERITANCE
class Student:
    def child(self):
        print("Hello GIET")
class S1(Student):
    def parent(self):
        print("Hello Parent")
s1 = S1()
s1.child()
s1.parent()