class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #курсы, которые закончил студент
        self.courses_in_progress = [] #курсы, которые сейчас изучаются
        self.grades = {} #оценки

    def lecturer_grades(self, course, grade, lecturer):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return round(mid_sum / len(self.grades.values()), 2) # УБРАЛА F-СТРОКУ, ОКРУГЛЯЕМ ДО 2 ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ

    def __lt__(self, other): # ПОДКОРРЕКТИРОВАЛА МЕТОДЫ. ДУМАЮ ТАК БУДЕТ ПРАВИЛЬНЕЕ
      if isinstance(other, Student):
        return self.average_grades() < other.average_grades()
      else:
        return 'Ошибка'

    def __gt__(self, other):
      if isinstance(other, Student):
        return self.average_grades() > other.average_grades()
      else:
        return 'Ошибка'


    def __eq__(self, other):
      if isinstance(other, Student):
        return self.average_grades() == other.average_grades()
      else:
        return 'Ошибка'

   def __str__(self):
        self.courses_in_progress = ", ".join(self.courses_in_progress)
        self.finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grades()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # закрепленные за преподавателем список курсов


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} # ДОБАВИЛА self

    def average_grades_lecturer(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return round(mid_sum / len(self.grades.values()), 2) # УБРАЛА F-СТРОКУ, ОКРУГЛЯЕМ ДО 2 ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ

    def __lt__(self, other): # ТАКЖЕ ПОДКОРРЕКТИРОВАЛА МЕТОДЫ
      if isinstance(other, Lecturer):
        return self.average_grades_lecturer() < other.average_grades_lecturer()
      else:
        return 'Ошибка'

    def __gt__(self, other):
      if isinstance(other, Lecturer):
        return self.average_grades_lecturer() > other.average_grades_lecturer()
      else:
        return 'Ошибка'


    def __eq__(self, other):
      if isinstance(other, Lecturer):
        return self.average_grades_lecturer() == other.average_grades_lecturer()
      else:
        return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grades_lecturer()}"







student1 = Student("Иван", "Иванов", "М")
student2 = Student("Анна", "Петрова", "Ж")
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student2.courses_in_progress +=

any_reviewer = Reviewer('Some', 'Buddy')
any_reviewer.courses_attached = ['Python', 'Git']

any_reviewer.rate_hw(student1, 'Python', 10)
any_reviewer.rate_hw(student1, 'Python', 8)
any_reviewer.rate_hw(student1, 'Git', 8)
any_reviewer.rate_hw(student1, 'Git', 7)

any_reviewer.rate_hw(student2, 'Python', 9)
any_reviewer.rate_hw(student2, 'Python', 10)
any_reviewer.rate_hw(student2, 'Git', 9)
any_reviewer.rate_hw(student2, 'Git', 6)



print(student1, student2, sep='\n')
print()
# ТУТ ВСЕ ОПЕРАТОРЫ РАБОТАЮТ. ВОЗВРАЩАЮТ TRUE или FALSE как обычные операторы сравнения. МОЖЕТЕ НАПИСАТЬ КОД, КОТОРЫЙ ПОКАЖЕТ КАКОЙ СТУДЕНТ ЛУЧШЕ. МОЖНО ОБЫЧНУЮ КОНСТРУКЦИЮ IF ELIF ПРЯМО ЗДЕСЬ. В КЛАССЕ ЭТО НЕОБЯЗАТЕЛЬНО ПРОПИСЫВАТЬ
print(student1 < student2)
print(student1 > student2)
print(student1 == student2)



lecturer1 = Lecturer("Петя", "Маслов")
lecturer2 = Lecturer("Вася", "Пупкин")
lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Git']
student1.lecturer_grades('Python', 8, lecturer1)
student1.lecturer_grades('Python', 10, lecturer1)
student1.lecturer_grades('Python', 10, lecturer1)

student1.lecturer_grades('Python', 9, lecturer2)
student1.lecturer_grades('Python', 7, lecturer2)
student1.lecturer_grades('Python', 10, lecturer2)
print()
print(lecturer1, lecturer2, sep='\n')
print()
# ТАКЖЕ МОЖЕТЕ ОПРЕДЕЛИТЬ ЛУЧШЕГО ЛЕКТОРА
print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)