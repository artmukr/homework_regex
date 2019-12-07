# task 42
import re


pattern = re.compile(r'https?://(www\.)?[a-zA-Z1-9]*\.[a-zA-Z1-9]*('
                     r'.[a-zA-Z1-9]*)?')


if __name__ == '__main__':
    links = """
    https://www.facebook.com
    http://google.com.ua
    https://www.ukrpravda.ua
    http://is_not_link
    is_not_link
    """
    matches = pattern.finditer(links)
    for match in matches:
        print(match.group())
