def get_keys_by_value(dictionary, target_value):
    keys = []
    for key, value in dictionary.items():
        if value == target_value:
            keys.append(key)
    return sorted(keys)


class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, name, score):
        self.students[name] = score

    def get_students(self):
        sorted_scores = sorted(set(self.students.values()))
        second_lower_score = sorted_scores[1]
        return get_keys_by_value(self.students, second_lower_score)


if __name__ == '__main__':
    db = StudentDatabase()
    input_n = int(input())
    if 2 <= input_n <= 5:
        for _ in range(input_n):
            name = input()
            score = float(input())
            db.add_student(name, score)

    else:
        raise Exception("Sorry, 2 <= N <= 5")

    for _ in db.get_students():
        print(_)
