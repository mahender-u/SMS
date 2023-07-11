class Student:
    count=0
    def __init__(self):
        print("non parameterized constructor")



s1=Student()
s1.count=30
print(s1.count)
