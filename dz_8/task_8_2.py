import re
def parser():
    RE_NAME = re.compile(
        r"""(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<resp>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)""")
    with open('nginx_logs.txt', 'r') as fr:
        print(*(tuple(x.groupdict().values())
                for line in fr for x in RE_NAME.finditer(line)), sep="\n")


if __name__ == "__main__":
    parser()
