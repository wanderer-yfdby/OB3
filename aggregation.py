class Teacher():
    def teach(self):
        print("Преподаватель учит")
class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher
    def start_lessone(self):
        self.teacher.teach()
# Пример агрегации
my_teacher = Teacher()
my_school = School(my_teacher)

my_school.start_lessone()
