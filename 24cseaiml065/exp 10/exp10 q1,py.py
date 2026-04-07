#Write a program to create a class for employee having member data:empid,name,basic pay,ta,da,gross payand member function:disp(),calc() use parameterized constructor to input the sample data.calc() to find gross pay=basicpay+10% of ta+40% of da. disp() to display the information implement desteructor to releasing memeory once use is over.input an employee details and print.
class Employee:
    def __init__(self, empid, name, basic_pay, ta, da):
        self.empid = empid
        self.name = name
        self.basic_pay = basic_pay
        self.ta = ta
        self.da = da
        self.gross_pay = 0.0

    def calc(self):
        self.gross_pay = self.basic_pay + (0.10 * self.ta) + (0.40 * self.da)

    def disp(self):
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Basic Pay: {self.basic_pay}")
        print(f"TA: {self.ta}")
        print(f"DA: {self.da}")
        print(f"Gross Pay: {self.gross_pay}")

    def __del__(self):
        print(f"Employee object for {self.name} is destroyed.")

empid = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
basic_pay = float(input("Enter Basic Pay: "))
ta = float(input("Enter TA: "))
da = float(input("Enter DA: "))

emp1 = Employee(empid, name, basic_pay, ta, da)

emp1.calc()
emp1.disp()

del emp1

