def add_ip(line: str):
    log = line.split('"')[0].split()[0]
    return log


def find_spamer(ip_lst: list):
    return max(set(ip_lst), key=ip_lst.count)


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for row in fr.readlines():
        list_out.append(add_ip(row))



print(f"ip спамера: {find_spamer(list_out)}")

