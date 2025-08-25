class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def find_student_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def list_students(self):
        return self.students

    def get_top_scorer(self, subject):
        top_student = None
        top_score = float('-inf')
        for s in self.students:
            score = s.scores.get(subject)
            if score is not None and score > top_score:
                top_score = score
                top_student = s
        return top_student

    def get_department_average(self, department):
        dept_scores = []
        for s in self.students:
            if s.department.lower() == department.lower() and s.scores:
                dept_scores.extend(s.scores.values())
        if not dept_scores:
            return 0
        return sum(dept_scores) / len(dept_scores)
