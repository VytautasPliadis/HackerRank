# import operator
#
# def person_lister(f):
#     def inner(people):
#         people.sort(key=lambda x: int(x[2]))
#         return [f(i) for i in people]
#     return inner
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')



def person_decorator(func):
    def wrapper(person):
        title = "Mr." if person[-1] == "M" else "Ms."
        return f"{title} {func(person)}"
    return wrapper

@person_decorator
def format_person(person):
    return f"{person[0]} {person[1]}"

if __name__ == "__main__":
    n = int(input())
    people = [input().split() for _ in range(n)]

    # Sort people by age in ascending order
    people.sort(key=lambda x: int(x[2]))

    # Print formatted names
    for person in people:
        print(format_person(person))

'''
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
'''