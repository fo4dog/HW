import csv
import sys

def show_sales(start, end):
    with open("bakery.csv", 'r', newline='', encoding='utf-8') as f_obj:
        score = 0
        reader = csv.reader(f_obj)
        for row in reader:
            score += 1
            if score >= start and score <= end and end != -1:
                print(row[0])
            elif end == -1:
                print(row[0])


if __name__ == '__main__':
    if len(sys.argv) == 3:
        start_f = int(sys.argv[1])
        end_f = int(sys.argv[2])
        show_sales(start_f, end_f)
    elif len(sys.argv) == 2:
        end_f = int(sys.argv[1])
        show_sales(1, end_f)
    else:
        show_sales(-1, -1)