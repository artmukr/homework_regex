# task 11
import re


pattern = re.compile(r'\S+[a-z.?!]$')


if __name__ == '__main__':
    sentence = "He wants to play PyGames."
    matches = pattern.finditer(sentence)
    for match in matches:
        print(match.group())
