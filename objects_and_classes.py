class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []      # прикреплённые курсы к предподавателям


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []      # завершенные курсы
        self.courses_in_progress = []   # курсы в процессе
        self.grades = {}                # оценки, словарь

    def rate_rw(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and
            course in lector.courses_attached and
            course in self.courses_in_progress and
                grade <= 10):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        list_grade = [i for v in self.grades.values() for i in v]
        process = ', '.join(self.courses_in_progress)
        finish = (', '.join(self.finished_courses)
                  if len(self.finished_courses) else 'Нет')

        if len(list_grade):
            average_rating = sum(list_grade) / len(list_grade)
        else:
            average_rating = sum(list_grade)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_rating}\n'
                f'Курсы в процессе изучения: {process}\n'
                f'Завершенные курсы: {finish}\n')

    def __lt__(self, other):
        self.list_grade = [i for list_grade in self.grades.values()
                           for i in list_grade]   # список оценок
        other.list_grade = [i for list_grade in other.grades.values()
                            for i in list_grade]  # список оценок
        if len(self.list_grade):
            self.average_rating = sum(self.list_grade) / len(self.list_grade)
        else:
            self.average_rating = sum(self.list_grade)
        if len(other.list_grade):
            other.average_rating = sum(
                other.list_grade) / len(other.list_grade)
        else:
            other.average_rating = sum(other.list_grade)

        self.fullname = self.name + ' ' + self.surname
        other.fullname = other.name + ' ' + other.surname

        if self.average_rating > other.average_rating:
            print(f'У студента {self.fullname} средняя оценка больше, '
                  f'чем у {other.fullname}\n')
        elif self.average_rating == other.average_rating:
            print('Средние оценки студентов равны.\n')
        else:
            print(f'У студента {self.fullname} средняя оценка меньше, '
                  f'чем у {other.fullname}\n')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []          # прикреплённые курсы к лекторам
        self.grades = {}                    # словарь с оценками от студентов

    def __str__(self):
        list_grade = [i for v in self.grades.values() for i in v]
        if len(list_grade):
            average_rating = sum(list_grade) / len(list_grade)
        else:
            average_rating = sum(list_grade)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_rating}\n')

    def __lt__(self, other):
        self.list_grade = [i for list_grade in self.grades.values()
                           for i in list_grade]   # список оценок
        other.list_grade = [i for list_grade in other.grades.values()
                            for i in list_grade]  # список оценок
        if len(self.list_grade):
            self.average_rating = sum(self.list_grade) / len(self.list_grade)
        else:
            self.average_rating = sum(self.list_grade)
        if len(other.list_grade):
            other.average_rating = sum(
                other.list_grade) / len(other.list_grade)
        else:
            other.average_rating = sum(other.list_grade)

        self.fullname = self.name + ' ' + self.surname
        other.fullname = other.name + ' ' + other.surname

        if self.average_rating > other.average_rating:
            print(f'У лектора {self.fullname} средняя оценка больше, '
                  f'чем у {other.fullname}\n')
        elif self.average_rating == other.average_rating:
            print('Средние оценки лекторов равны.\n')
        else:
            print(f'У лектора {self.fullname} средняя оценка меньше, '
                  f'чем у {other.fullname}\n')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []       # прикреплённые курсы к ревьюерам

    def rate_rw(self, student, course, grade):
        if (isinstance(student, Student)
            and course in student.courses_in_progress
            and course in self.courses_attached
                and grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


def average_grade_student(list_students, course):
    '''Средняя оценка за домашние задания студентов по курсу'''
    list_grade = [
        # список оценок по курсу
        i for student in list_students for i in student.grades[course]]
    # средняя оценка по курсу
    average_grade = sum(list_grade) / len(list_grade)
    return 'Средняя оценка за домашние задания '\
           f'по курсу {course}: {average_grade}\n'


def average_grade_lectors(list_lectors, course):
    '''Средняя оценка за лекции лекторов по курсу'''
    list_grade = [
        # список оценок по курсу
        i for lector in list_lectors for i in lector.grades[course]]
    # средняя оценка по курсу
    average_grade = sum(list_grade) / len(list_grade)
    return 'Средняя оценка за лекции '\
           f'по курсу {course}: {average_grade}\n'


student1 = Student('Андрей', 'Булыгин', 'м')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Тестировщик с нуля']

student2 = Student('Максим', 'Казаков', 'м')
student2.courses_in_progress += ['Python']

lector1 = Lecturer('Илья', 'Веселов')
lector1.courses_attached += ['Python']

lector2 = Lecturer('Петр', 'Иванов')
lector2.courses_attached += ['Python']

reviewer1 = Reviewer('Олег', 'Добровольский')
reviewer2 = Reviewer('Василий', 'Копылов')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

student1.rate_rw(lector1, 'Python', 5)
student1.rate_rw(lector2, 'Python', 7)
student2.rate_rw(lector1, 'Python', 8)
student2.rate_rw(lector2, 'Python', 9)

reviewer1.rate_rw(student1, 'Python', 10)
reviewer1.rate_rw(student2, 'Python', 8)

reviewer2.rate_rw(student1, 'Python', 10)
reviewer2.rate_rw(student2, 'Python', 6)

print(student1)
print(student2)
print(lector1)
print(lector2)
print(reviewer1)
print(reviewer2)

student1.__lt__(student2)
lector1.__lt__(lector2)

print(average_grade_student([student1, student2], 'Python'))
print(average_grade_lectors([lector1, lector2], 'Python'))
