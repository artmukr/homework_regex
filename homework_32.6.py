# task 50
import re


pattern = re.compile(r'([a-z1-9]+)\s?(\(\.com\))?')


if __name__ == '__main__':
    links = """
    example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)
    """
    matches = pattern.finditer(links)
    for match in matches:
        print(match[1])
