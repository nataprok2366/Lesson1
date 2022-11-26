# class Student:
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info (self):
#         print(f'Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}')
#
# s1 = Student("Natalya", 'Prokopechko', 12)
# s1.info()




class Average:
    def __init__(self, one, two, three, four, five, six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

    def info (self):
        print(f'Number1: {self.one}\nNumber2: {self.two}\nNumber3: {self.three}\nNumber4: {self.four}\nNumber5: {self.five}\nNumber6: {self.six}')

s1 = Average(1,2,3,4,5,6,)
s1.info()
res = 1+2+3+4+5+6
print(res /6)
