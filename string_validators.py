class StrValidator:
    def __init__(self): #cia biski pakoreguot
        self.input_list = list(input_list.replace(" ", "")) #cia biski pakoreguot
        self.alphanumeric = False
        self.letters = False
        self.decimals = False
        self.lower_char = False
        self.upper_char = False
        if len(self.input_list) > 1000:
            raise ValueError('Max 1000 chars')

    def __setattr__(self, input_list, **kwargs):  #cia biski pakoreguot
        if len(self.input_list) > 1000:
            raise ValueError('Max 1000 chars')
        super().__setattr__(input_list)  # Call the parent class's __setattr__ method

    def __call__(self):
        for _ in self.input_list:
            if _.isalnum():
                self.alphanumeric = True
            if _.isalpha():
                self.letters = True
            if _.isdecimal():
                self.decimals = True
            if _.islower():
                self.lower_char = True
            if _.isupper():
                self.upper_char = True

    def __str__(self):
        return f'{self.alphanumeric}\n{self.letters}\n{self.decimals}\n{self.lower_char}\n{self.upper_char}'


if __name__ == '__main__':
    string1 = StrValidator(input())
    print(string1)
