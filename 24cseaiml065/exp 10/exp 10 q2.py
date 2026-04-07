#write a program to create four base classes having individual method addition(),subtraction(),multiplication(),division() respectively. create a derived class for all above (multiple inheritance) having member data: data1,data2 . create an objest and then perform operation on the data 1 and data 2
class Adder:
    def addition(self, data1, data2):
        return data1 + data2

class Subtractor:
    def subtraction(self, data1, data2):
        return data1 - data2

class Multiplier:
    def multiplication(self, data1, data2):
        return data1 * data2

class Divider:
    def division(self, data1, data2):
        if data2 != 0:
            return data1 / data2
        else:
            return "Error: Division by zero"

class Calculator(Adder, Subtractor, Multiplier, Divider):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

calc_object = Calculator(10, 5)

sum_result = calc_object.addition(calc_object.data1, calc_object.data2)
difference_result = calc_object.subtraction(calc_object.data1, calc_object.data2)
product_result = calc_object.multiplication(calc_object.data1, calc_object.data2)
quotient_result = calc_object.division(calc_object.data1, calc_object.data2)

print(f"Addition: {sum_result}")
print(f"Subtraction: {difference_result}")
print(f"Multiplication: {product_result}")
print(f"Division: {quotient_result}")
                       