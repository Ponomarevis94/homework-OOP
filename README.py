lecturer_list = []
students_list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_lec(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade_lecturer <=10:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade_lecturer]
            else:
                lecturer.grades_lecturer[course] = [grade_lecturer]
        else:
            return 'Ошибка'

    def average_grades(self):
        all_grades_stud = []
        if not self.grades.values():
            return f'У студента {self.name} нет оценок'
        else:
            for marks in self.grades.values():
                for mark in marks:
                    all_grades_stud.append(mark)
            return round(sum(all_grades_stud) / len(all_grades_stud), 1)
    
    def __gt__(self, other):
        if self.average_grades() == f'У студента {self.name} нет оценок' or other.average_grades() == f'У студента {self.name} нет оценок':
            return 'Невозможно сравнить'
        else:
            return self.average_grades() > other.average_grades()

    def __str__(self):
        some_student = f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашнее задание: {self.average_grades()}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}
        """
        return some_student 

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __str__(self):
        return f"""
           Имя: {self.name}
           Фамилия: {self.surname}
           """

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}
        lecturer_list.append(self)

    def average_grades_lec(self):
        all_grades_lec = []
        if not self.grades_lecturer.values():
            return f'У лектора {self.name} нет оценок'
        else:
            for marks in self.grades_lecturer.values():
                for mark in marks:
                    all_grades_lec.append(mark)
            return round(sum(all_grades_lec) / len(all_grades_lec), 1) 

    def __gt__(self, other):
        if self.average_grades_lec() == f'У лектора {self.name} нет оценок' or other.average_grades_lec() == f'У лектора {self.name} нет оценок':
            return 'Невозможно сравнить'
        else:
            return self.average_grades_lec() > other.average_grades_lec()

    def __str__(self):
        some_lecturer = f"""
           Имя: {self.name}
           Фамилия: {self.surname}
           Средняя оценка за лекции:{self.average_grades_lec()}
           """
        return some_lecturer

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
        some_reviewer = f"""
           Имя: {self.name}
           Фамилия: {self.surname}
           """
        return some_reviewer

def average_course_lec(lecturer_list, course):
    grades_list_lec = []
    for lecturer in lecturer_list:
        if not course in lecturer.courses_attached:
            print(f'Преподаватель {lecturer.name} не ведет лекции по курсу: {course}')
        elif not course in lecturer.grades_lecturer:
            print(f'У преподавателя {lecturer.name} нет оценок за курс: {course}')
        else:
            for mark in lecturer.grades_lecturer[course]:
                grades_list_lec.append(mark)
    if len(grades_list_lec) == 0:
        return 'Ошибка, у преподавателей нет оценок!'
    else:
        return f'Средняя оценка всех лекторов в рамках курса {course}: {round(sum(grades_list_lec) / len(grades_list_lec), 1)}'

def average_course_stud(students_list, course):
    grades_list_stud = []
    for student in students_list:
        if not course in student.courses_in_progress:
            print(f'Студент {student.name} не изучает курс {course}')
        elif not course in student.grades:
            print(f'У студентa {student.name} нет оценок за курс: {course}')
        else:
            for mark in student.grades[course]:
                grades_list_stud.append(mark)
    if len(grades_list_stud) == 0:
        return 'Ошибка у студентов нет оценок!'
    else:
        return f'Средняя оценка всех студентов в рамках курса {course}: {round(sum(grades_list_stud) / len(grades_list_stud), 1)}'
 

 
student_1 = Student('Илья', 'Муромец', 'мужской')
student_1.add_courses('Тестировщик ПО')
student_1.courses_in_progress += ['Python-разработчик']

student_2 = Student('Алеша', 'Попович', 'мужской')
student_2.add_courses('Python-разработчик')
student_2.courses_in_progress += ['Тестировщик ПО']

reviewer_1 = Reviewer('Добрыня ', 'Никитич')
reviewer_1.courses_attached += ['Python-разработчик']

reviewer_2 = Reviewer('Елисей','Силович')
reviewer_2.courses_attached += ['Тестировщик ПО']

lecturer_1 = Lecturer('Забава', 'Путятишна')
lecturer_1.courses_attached += ['Python-разработчик']

lecturer_2 = Lecturer('Настасья', 'Филиповна')
lecturer_2.courses_attached += ['Тестировщик ПО']

reviewer_1.rate_hw(student_1,'Python-разработчик', 10)
reviewer_1.rate_hw(student_1,'Python-разработчик', 8)
reviewer_2.rate_hw(student_2,'Тестировщик ПО', 7)
reviewer_2.rate_hw(student_2,'Тестировщик ПО', 10)

student_1.rate_lec(lecturer_1, 'Python-разработчик', 7)
student_1.rate_lec(lecturer_1, 'Python-разработчик', 8)
student_2.rate_lec(lecturer_2, 'Тестировщик ПО', 10)
student_2.rate_lec(lecturer_2, 'Тестировщик ПО', 9)

print(f'Студент 1: {student_1}')
print(f'Студент 1: {student_2}')

print(f'Ревьюер 1: {reviewer_1}')
print(f'Ревьюер 2: {reviewer_2}')

print(f'Лектор 1: {lecturer_1}')
print(f'Лектор 2: {lecturer_2}')

print(student_1 < student_2)
print(student_1 > student_2)
print(student_1 == student_2)
print(student_1 != student_2)

print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)

print(average_course_stud(students_list,'Python-разработчик'))
print(average_course_stud(students_list,'Тестировщик ПО'))

print(average_course_lec(lecturer_list,'Python-разработчик'))
print(average_course_lec(lecturer_list,'Тестировщик ПО'))