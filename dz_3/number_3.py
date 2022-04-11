def thesaurus(*args) -> dict:
    dict_out = {}
    for i in args:
        if dict_out.get(i[0]) is None:
            dict_out[i[0]] = i.split()
        else:

            dict_update = dict_out.get(i[0])
            dict_update.append(i)
            dict_out[i[0]] = dict_update
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Владислав", "Владимир"))
