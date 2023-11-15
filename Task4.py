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
            return round(mid_sum / len(self.grades.values()), 2)

    def __lt__(self, other):
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
        self.courses_attached = []


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
        self.grades = {}

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
            return round(mid_sum / len(self.grades.values()), 2)

    def __lt__(self, other):
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

print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)

# Создаем список студентов
student_list = [student_1, student_2, student_3]

# Создаем список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()