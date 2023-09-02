class StrValidator:
    def __init__(self, input_list):
        self.input_list = list(input_list.strip())
        if len(self.input_list) > 1000:
            raise ValueError('Max 1000 chars')
        self.alphanumeric = any(char.isalnum() for char in self.input_list)
        self.letters = any(char.isalpha() for char in self.input_list)
        self.decimals = any(char.isdecimal() for char in self.input_list)
        self.lower_char = any(char.islower() for char in self.input_list)
        self.upper_char = any(char.isupper() for char in self.input_list)

    def __str__(self):
        return f'{self.alphanumeric}\n{self.letters}\n{self.decimals}\n{self.lower_char}\n{self.upper_char}'


if __name__ == '__main__':
    input_string = input()
    string1 = StrValidator(input_string)
    print(string1)
