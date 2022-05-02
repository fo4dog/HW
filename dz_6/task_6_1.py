from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    log_ip = line.split('"')[0].split()[0]
    log_type = line.split('"')[1].split()[0]
    log_resource = line.split('"')[1].split()[1]
    yield log_ip, log_type, log_resource


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for row in fr.readlines():
        list_out.append(*get_parse_attrs(row))

pprint(list_out)











