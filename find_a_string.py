class FindSting:
    def __init__(self, text_string, text_sub_string):
        self.string = text_string
        self.sub_string = text_sub_string

    def count_substring(self):
        if not 1 <= len(self.string) <= 200:
            raise ValueError('String is too big or to small. Max len 200')

        count = 0
        index = self.string.find(self.sub_string)

        while index != -1:
            count += 1
            index = self.string.find(self.sub_string, index + 1)

        return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    result = FindSting(string, sub_string).count_substring()
    print(result)
