tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Вова', 'Алексей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    for child in range(0, len(tutors)+1):
        if child + 1 > len(klasses):
            yield (tutors[child], None)
        else:
            yield (tutors[child], klasses[child])
generator = check_gen(tutors, klasses)
print(type(generator))
# добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration