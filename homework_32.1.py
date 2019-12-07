# task 4
import re


pattern = re.compile(r'[a-zA-Z0-9]+(a0|ab)[a-zA-Z0-9]+')


if __name__ == '__main__':
    string_find = """
    test1a0test2
    3testabbtest
    shagdhgabbsdhhfjhd
    kdgskfhkjdfhj
    """
    matches = pattern.finditer(string_find)
    for match in matches:
        print(match.group())
