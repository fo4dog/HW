def thesaurus_adv(*args) -> dict:
    dict_out = {}
    for input_string in args:

        input_list = input_string.split()
        first = input_list[0][0]
        last = input_list[1][0]
        if last not in dict_out.keys():
            dict_out.update({last: {first : [input_string]}})
        else:
            dict_of_names = dict_out.get(last)
            if first not in dict_of_names.keys():
                dict_of_names.update({first: [input_string]})
                dict_out.update({last: dict_of_names})
            else:
                output_str = [' '.join(input_string.split()), ' '.join(dict_of_names.get(first))]
                dict_of_names.update({first: output_str})
                dict_out.update({last: dict_of_names})
    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Александр Соколов"))
