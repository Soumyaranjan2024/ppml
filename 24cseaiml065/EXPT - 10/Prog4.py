#METHOD OVERRIDING
class Parent:
    def show(self):
        print("Parent's show method")
class Child(Parent):
    def show(self):
        print("Child's show method")
c = Child()
c.show()