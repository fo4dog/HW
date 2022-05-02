import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_NAME = re.compile(
        r"(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")
    try:
        test = list(map(lambda x: x.groupdict(), RE_NAME.finditer(email)))
        return test[0]
    except:
        raise ValueError from ValueError


if __name__ == '__main__':
    print(email_parse('some_one_ner@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))