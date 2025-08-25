class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.scores = {}

    def add_score(self, subject, marks):
        self.scores[subject] = marks

    def get_average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def __str__(self):
        scores_str = ', '.join(
            [f"{sub}: {marks}" for sub, marks in self.scores.items()])
        return (f"ID: {self.student_id}\n"
                f"Name: {self.name}\n"
                f"Department: {self.department}\n"
                f"Scores: {scores_str}\n"
                f"Average Score: {self.get_average_score():.2f}")
