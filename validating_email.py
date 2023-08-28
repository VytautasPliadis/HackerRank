import re


def fun(s):
    pattern = r'^[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.+[A-Za-z]{2,3}$'
    # r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.+[A-Za-z]{2,}$'
    return re.match(pattern, s) is not None


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
