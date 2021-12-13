
class Student:

    instances = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.instances.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_raiting(self):
        sum_grade = 0
        count_grade = 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            count_grade += len(grade)
        if count_grade == 0:
            return count_grade
        return sum_grade / count_grade

    def __str__(self):
        return f'Имя: {self.name} \
                \nФамилия: {self.surname} \
                \nСредняя оценка за домашние задания: {round(self._average_raiting(), 2)}\
                \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
                \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, some_student):
        if not isinstance(some_student, Student):
            print('Ошибка типов')
            return
        else:
            return self._average_raiting() < some_student._average_raiting()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    instances = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.instances.append(self)

    def _average_raiting(self):
        sum_grade = 0
        count_grade = 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            count_grade += len(grade)
        if count_grade == 0:
            return count_grade
        return sum_grade / count_grade
    
    def __str__(self):
        return f'Имя: {self.name} \
                \nФамилия: {self.surname} \
                \nСредняя оценка за лекции: {round(self._average_raiting(), 1)}'

    def __lt__(self, some_lecturer):
        if not isinstance(some_lecturer, Lecturer):
            print('Ошибка типов')
            return
        else:
            return self._average_raiting() < some_lecturer._average_raiting()


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
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def avg_by_lecturers_on_course(list_of_lecturers, course):
    sum_grade = 0
    count_grade = 0
    for lecturer in list_of_lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            sum_grade += sum(lecturer.grades[course])
            count_grade += len(lecturer.grades[course])
    if count_grade == 0:
        return count_grade
    return sum_grade / count_grade


def avg_by_students_on_course(list_of_students, course):
    sum_grade = 0
    count_grade = 0
    for student in list_of_students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            sum_grade += sum(student.grades[course])
            count_grade += len(student.grades[course])
    if count_grade == 0:
        return count_grade
    return sum_grade / count_grade


student_1 = Student('Антон', 'Антоныч', 'муж')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Андрей', 'Андреич', 'муж')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Иван', 'Иваныч')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Введение в программирование']

lecturer_2 = Lecturer('Максим', 'Максимыч')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Василий', 'Васильевич')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Введение в программирование']

reviewer_2 = Reviewer('Михал', 'Михалыч')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 10)

reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 10)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 9)

print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)

print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
            
print(f"Средняя оценка по всем студентам по курсу Python {avg_by_students_on_course(Student.instances, 'Python')}")
print(f"Средняя оценка по всем студентам по курсу Git {avg_by_students_on_course(Student.instances, 'Git')}")
print(avg_by_students_on_course(Student.instances, 'Введение в программирование'))

print(f"Средняя оценка за лекции всех лекторов по курсу Python {avg_by_lecturers_on_course(Lecturer.instances, 'Python')}")
print(f"Средняя оценка за лекции всех лекторов по курсу Git {avg_by_lecturers_on_course(Lecturer.instances, 'Git')}")
        
