def swap_case(s):
    # char_list = []
    # for i in s:
    #     if i.islower():
    #         char_list.append(i.upper())
    #     elif i.isupper():
    #         char_list.append(i.lower())
    #     else:
    #         char_list.append(i)
    # joined_chars = ''.join(char_list)
    # return joined_chars

    return ''.join([i.upper() if i.islower() else i.lower() for i in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
