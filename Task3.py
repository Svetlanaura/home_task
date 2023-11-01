class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def rate_hw(self, lecturer, course, grades):
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grades]
                else:
                    lecturer.grades[course] = [grades]
            else:
                return 'Ошибка'

            def __str__(self):

                return ("f Имя {self.name}\n"
                        f"Фамилия {self.surname}\n"
                        f"Средняя оценка {self.average_grades}\n"
                        f"Курсы в процессе изучения {self.courses_in_progress}\n"
                        f"Завершеннные курсы {self.finished_courses}\n")

    def assign_lecturer(self, lecturer):
        if self.course in lecturer.courses:
            self.lecturer = lecturer
            lecturer.students.append(self)
        else:
            print(f"{lecturer.name} не является лектором по курсу {self.course}")

    def rate_lecturer(self, rating):
        if self.lecturer:
            self.lecturer.add_rating(self.course, rating)
        else:
            print("Студент не имеет закрепленного лектора")

    def __str__(self):
        return f"Студент: {self.name}, курс: {self.course}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def add_rating(self, course, rating):
        if course not in self.students:
            self.students[course] = []
        self.students[course].append(rating)

    def get_avg_rating(self, course):
        if course in self.students:
            ratings = self.students[course]
            return sum(ratings) / len(ratings)
        else:
            print(f"Нет оценок для курса {course}")

    def __str__(self):
        return ("f Имя {self.name}\n"
                f"Фамилия {self.surname}\n"
                f"Средняя оценка {self.average_grades}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        def __str__(self):
            return ("f Имя {self.name}\n"
                    f"Фамилия {self.surname}")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
