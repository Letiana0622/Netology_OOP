class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#метод для выставления оценок лекторам студентами
# Задание № 2.Атрибуты и взаимодействие  классов.
# Возможность (метод) выставлять оценки студентам только у Reviewer
# Возможность (метод) получать оценки  за лекции от студентов:) для Лекторов у Студентов
# оценки по 10 - балльной  шкале, хранятся  ватрибуте - словаре у Lecturer,
# в котором ключи – названия курсов, а  значения – списки оценок.
# Лектор при этом должен быть  закреплен за тем курсом, на который записан студент.

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Перегрузите магический метод __str__ у всех классов.
# А у студентов так:
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

    def average_grades(self):
        grade_list_student = []
        grade_sum = 0
        for course, grades in self.grades.items():
            for grade in grades:
                grade_list_student.append(grade)
        for grade in grade_list_student:
            grade_sum = grade_sum + grade
        # grade_sum = sum(grade_list_student)
        grade_average_student = round(int(grade_sum)/ int(len(grade_list_student)),2)
        return grade_average_student

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_grades()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'

# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grades() < other.average_grades()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов
# (вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения,
# а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и
# Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
# А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

# Перегрузите магический метод __str__ у всех классов.
# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

    def average_grades(self):
       grade_list_lecturer = []
       grade_sum = 0
       for course, grades in self.grades.items():
           for grade in grades:
               grade_list_lecturer.append(grade)
       for grade in grade_list_lecturer:
           grade_sum = grade_sum + grade
       grade_average_lecturer = sum(grade_list_lecturer)/len(grade_list_lecturer)
       return grade_average_lecturer

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_grades()}'


class Reviewer(Mentor):
    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

# Задание № 4. Полевые испытания. # Создайте по 2 экземпляра каждого класса, вызовите все созданные методы,
# а также реализуйте две функции:для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# в качестве аргументов принимаем список студентов и название курса):

def average_grades_course_students(course, students_list):
    grade_sum_course = 0
    counter = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grade_sum_course += student.average_grades()
            counter += 1
    grade_average_course = int(grade_sum_course)/int(counter)
    print(grade_average_course)

# Задание № 4.реализуйте две функции:для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).

def average_grades_course_lecturers(course, lecturers_list):
    grade_sum_course = 0
    counter = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grade_sum_course += lecturer.average_grades()
            counter += 1
    grade_average_course = int(grade_sum_course)/int(counter)
    print(grade_average_course)


# Задание № 4. Полевые испытания. # Создайте по 2 экземпляра каждого класса, вызовите все созданные методы:

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

worst_student = Student('Baunty', 'Hunter', 'your_gender')
worst_student.finished_courses += ['Git']
worst_student.courses_in_progress += ['Python']
worst_student.grades['Git'] = [1, 1, 1, 1, 1]
worst_student.grades['Python'] = [2, 2, 2]

print()
print(f"Best student's completed courses is  {best_student.finished_courses}")
print(f"Best student's course in progress is {best_student.courses_in_progress}")
print(f"Best student's grades per each course are {best_student.grades}")

print()
print(f"Best student's completed courses is  {worst_student.finished_courses}")
print(f"Best student's course in progress is {worst_student.courses_in_progress}")
print(f"Best student's grades per each course are {worst_student.grades}")


print()
print('Cредняя оценка студентов по курсу Python:')
average_grades_course_students('Python', [best_student, worst_student])
print()


print('Перезагрузка __str__  для best_student ')
print(best_student.__str__())
print()
print('Перезагрузка __str__  для worst_student ')
print(worst_student.__str__())
print()

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer.rate_hw_student(best_student, 'Python', 5)
cool_reviewer.rate_hw_student(worst_student, 'Python', 10)
print(f"Cool reviewer's courses are {cool_reviewer.courses_attached}")
print(f"Best student's grades for courses in progress after cool reviewer check are {best_student.grades}")
print()
print('Перезагрузка __str__  для cool_reviewer')
print(cool_reviewer.__str__())

some_lecturer = Lecturer('Tutti', 'Frutti')
some_lecturer.courses_attached += ['Git', 'Python']
some_lecturer.grades['Git'] = [2, 7, 10]
ghost_lecturer = Lecturer('Tom', 'Rider')
ghost_lecturer.courses_attached += ['Python', 'Git']
ghost_lecturer.grades['Git'] = [5, 5, 5]
print(f"Some lecturer's courses are  {some_lecturer.courses_attached}")
print(f"Some lecturer's ratings from students are {some_lecturer.grades}")
print(f"Ghost lecturer's courses are  {ghost_lecturer.courses_attached}")
print(f"Ghost lecturer's ratings from students are {ghost_lecturer.grades}")

print()
print('Cредняя оценка лекторов по курсу Git:')
average_grades_course_lecturers('Git', [some_lecturer, ghost_lecturer])

print()
best_student.rate_hw_lecturer(some_lecturer, 'Git', 5)
best_student.rate_hw_lecturer(some_lecturer, 'Python', 10)
worst_student.rate_hw_lecturer(ghost_lecturer, 'Git', 1)
worst_student.rate_hw_lecturer(ghost_lecturer, 'Python', 5)
print(f"Some lecturer's ratings after best student feedback for finished course are {some_lecturer.grades}")

print()
print('Перезагрузка __str__  для some_lecturer')
print(some_lecturer.__str__())
print()
print('Перезагрузка __str__  для ghost_lecturer')
print(ghost_lecturer.__str__())
print()
print('Перезагрузка __lt__ для сравнения средней оценки студента к средней оценке лектора(пример: best_student < some_lecturer)')
print(best_student.__lt__(some_lecturer))




