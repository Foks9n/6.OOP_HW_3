class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self, count):
        """ Подсчитывает среднее значение заданного объекта, универсальный метод """
        return round(sum(sum(count.values(), [])) / len(sum(count.values(), [])), 1)


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average(self.grades)}'
                f' \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, Student):
        return self.average < Student.average

    def __gt__(self, Student):
        return self.average > Student.average

    def __eq__(self, Student):
        return self.average == Student.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average(self, count):
        """ Подсчитывает среднее значение заданного объекта, универсальный метод """
        return round(sum(sum(count.values(), [])) / len(sum(count.values(), [])), 1)


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average(self.grades)}')


    def __lt__(self, Lecturer):
        return self.average < Lecturer.average

    def __gt__(self, Lecturer):
        return self.average > Lecturer.average

    def __eq__(self, Lecturer):
        return self.average == Lecturer.average


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}')


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'JS']
some_student.finished_courses += ['Введение в программирование']


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['JS', 'Python']

some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'JS', 6)
some_student.rate_hw(some_lecturer, 'Python', 8)
#
# print(some_lecturer.grades)
#
some_reviewer = Reviewer('Snoop', 'Dogg')
some_reviewer.courses_attached += ['Python', 'JS']
some_reviewer.rate_hw(some_student, 'Python', 2)
some_reviewer.rate_hw(some_student, 'Python', 5)
some_reviewer.rate_hw(some_student, 'JS', 10)
#
# print(some_student.grades)

print(some_student)
print(some_reviewer)
print(some_lecturer)