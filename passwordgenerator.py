import random


class PWD:
    def __init__(self, number=16):
        self.num = number

    @staticmethod
    def generate_password():
        num = 20
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                             'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                             'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                   '*', '(', ')']

        characters = [DIGITS, SYMBOLS, UPCASE_CHARACTERS, LOCASE_CHARACTERS]

        password = ""

        for i in range(num):
            x = random.choice(characters)
            password += random.choice(x)

        # sr = ''.join(random.sample(password, len(password)))

        return password


if __name__ == '__main__':
    pass_w = PWD.generate_password()
    print(pass_w)
