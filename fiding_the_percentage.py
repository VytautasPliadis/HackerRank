class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student_marks(self):
        name, *line = input().split()
        scores = list(map(float, line))
        self.students[name] = scores
        for i in scores:
            if (i < 0) or (i > 100):
                raise Exception("Sorry, 0 <= score <= 100")

    def get_students(self, name):
        scores = self.students.get(name)
        avg = sum(scores)/len(scores)
        avg = round(avg, 2)
        return "{:.2f}".format(avg)


if __name__ == '__main__':
    n = int(input())
    if (n < 2) or (n > 10):
        raise Exception("Sorry, 2 <= N <= 10")
    db = StudentDatabase()
    for _ in range(n):
        db.add_student_marks()
    print(db.get_students(input()))