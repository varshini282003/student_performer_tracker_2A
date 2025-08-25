from models.student import Student


class Graduate(Student):
    def __init__(self, student_id, name, department, thesis_title):
        super().__init__(student_id, name, department)
        self.thesis_title = thesis_title

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}\nThesis Title: {self.thesis_title}"
