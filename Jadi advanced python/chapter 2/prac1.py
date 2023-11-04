class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight


class Class:
    def __init__(self, name, num_student):
        self.name = name
        self.num_student = num_student
        self.students = []
        self.mean_age = 0
        self.mean_height = 0
        self.mean_weight = 0
    
    def add_student(self, student):
        self.students.append(student)
        self.mean_age = sum([s.age for s in self.students]) / len(self.students)
        self.mean_height = sum([s.height for s in self.students]) / len(self.students)
        self.mean_weight = sum([s.weight for s in self.students]) / len(self.students)


class_a = Class('A', int(input()))

a_ages = list(int(i) for i in (input().split(' ')))
a_heights = list(int(i) for i in (input().split(' ')))
a_weights = list(int(i) for i in (input().split(' ')))

for i in range(class_a.num_student):
    class_a.add_student(Student(a_ages[i], a_heights[i], a_weights[i]))


class_b = Class('B', int(input()))

b_ages = list(int(i) for i in (input().split(' ')))
b_heights = list(int(i) for i in (input().split(' ')))
b_weights = list(int(i) for i in (input().split(' ')))

for i in range(class_b.num_student):
    class_b.add_student(Student(b_ages[i], b_heights[i], b_weights[i]))

print(class_a.mean_age)
print(class_a.mean_height)
print(class_a.mean_weight)
print(class_b.mean_age)
print(class_b.mean_height)
print(class_b.mean_weight)

if class_a.mean_height > class_b.mean_height :
    print('A')
elif class_b.mean_height > class_a.mean_height :
    print('B')
else:
    if class_a.mean_weight > class_b.mean_weight :
        print('A')
    elif class_b.mean_weight > class_a.mean_weight :
        print('B')
    else:
        print('Same')