def get_keys_by_value(dictionary, target_value):
    """
    Retrieve keys from a dictionary that match a specific value.

    Args:
        dictionary (dict): The dictionary to search in.
        target_value: The value to match in the dictionary.

    Returns:
        list: A sorted list of keys that correspond to the target value.
    """
    keys = []
    for key, value in dictionary.items():
        if value == target_value:
            keys.append(key)
    return sorted(keys)


class StudentDatabase:
    """
        A class representing a student database.

        Attributes:
            students (dict): A dictionary to store student names as keys and their scores as values.

        Methods:
            add_student(name, score):
                Add a student to the database with their name and score.
            get_students():
                Retrieve a sorted list of student names who have the second lowest score.
    """
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
