class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #список студентів
        self.teachers = [] #1 завдання
        self.classes = [] #2 завдання
    def admit_student(self, student): #зарахування студентів
        self.students.append(student)
        print(f'{student.name} був доданий до школи {self.name}') #дописати, коли створимо клас студентів
    def expel_student(self, student):
        expelled_student =  next(filter(lambda s: s.name == student.name
                                                  and s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} не був знайдений {self.name}')
    #1 завдання
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f'{teacher.name} був доданий до {self.name}')
    #2 завдання
    def add_class(self, class_obj):
        self.classes.append(class_obj)
        print(f'Клас під номером {class_obj.number} був доданий до {self.name}')
    #3 завдання
    def get_school_statistic(self):
        num_students = len(self.students)
        if num_students == 0:
            avg_grade = 0
        else:
            avg_grage = sum(student.grade for student in self.students) / num_students #avg_grage = get_avarage_grade()
        return f'На {num_students} студентів середня оцінка по школі дорівінює {avg_grage}'

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade +=  1
        print(f'{self.name} був підвищений {self.grade}')
    def demote(self):
        self.grade -=  1
        print(f'{self.name} був понижений {self.grade}')
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'



lisa = Student("Alisa", 6)
masha = Student("Maria", 2)
andriiko = Student("Andriy", 50)
dima = Student("Dmytro", 23)
gleb = Student("Gleb", 100)
my_school = School("ItStep", [lisa, masha, andriiko, dima, gleb])
print("Початкові студенти: ")

for student in my_school.students:
    print(student)

my_school.admit_student(Student("Bogdan", 3))
my_school.expel_student(Student("Alisa", 6))
print("Оновлення: ")
for student in my_school.students:
    print(student)



#перше завдання
class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes
#друге завдання
class Class:
    def __init__(self, number):
        self.number = number
        self.students = []
    def add_student(self, student):
        self.students.append(student)
        print(f'{student.name} був доданий до {self.number} класу')
#третє завдання
    def get_avarage_grade(self):
        total_grades = 0
        for student in self.students:
            total_grades += student.grade
        return total_grades / len(self.students)

class1 = Class(1111)
class2 = Class(1121)  #створюємо клас

my_school.add_class(class1)
my_school.add_class(class2) #додаємо до школи

class1.add_student(lisa)
class2.add_student(dima)
class1.add_student(andriiko)
class2.add_student(gleb)  #додаємо учнів до класів у школі

teacher_1 = Teacher('Vova', 'PE', class2)
teacher_2 = Teacher('Anastasia', 'Physique', class1)   #створюємо вчителів
my_school.add_teacher(teacher_1)
my_school.add_teacher(teacher_2)  #додаємо вчителів до школи

l = []
for class_obj in my_school.classes:
    l.append(class_obj.number)
print(f'Список класів: {l}')                         #print номери класів
for teacher in my_school.teachers:
    print(f'{teacher.name} є вчителем у класі {class_obj.number}')   #виводим імена вчителів

print(my_school.get_school_statistic())  #return середню статистику

print(f'Середні бал у класі під номером {class1.number} : {class1.get_avarage_grade()}')
print(f'Середні бал у класі під номером {class2.number} : {class2.get_avarage_grade()}')   #середня оцйінка по класам