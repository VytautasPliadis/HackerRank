def count_substring(string, sub_string):
    if not 1 <= len(string) <= 200:
        raise ValueError('String is too big or to small. Max len 200')

    count = 0
    index = string.find(sub_string)

    while index != -1:
        count += 1
        index = string.find(sub_string, index + 1)

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
