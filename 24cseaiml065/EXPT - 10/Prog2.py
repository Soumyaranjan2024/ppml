#MULTILEVEL INHERITANCE
class Grandparent:
    def property(self):
        print("Property")
class Parent(Grandparent):
    def business(self):
        print("Business")
class Child(Parent):
    def education(self):
        print("Education")
c = Child()
c.property()
c.business()
c.education()