# task 10
import re


pattern = re.compile(r'^[a-zA-Z1-9]*')

if __name__ == '__main__':
    sentence = "He wants to play PyGames."
    matches = pattern.finditer(sentence)
    for match in matches:
        print(match.group())
