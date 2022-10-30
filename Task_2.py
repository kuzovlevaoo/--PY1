def get_count_char(str_):
    dict_letter = {}
    str_ = str_.lower()

    for i in str_:
        if i.isalpha():
            if i in dict_letter:
                dict_letter[i] += 1
            else:
                dict_letter[i] = 1
    return dict_letter

def letter_percentage(dict_):
    dict_percentage = dict_.copy()
    total_sum_letters = sum(dict_.values())
    for i in dict_percentage.keys():
        dict_percentage[i]=round(dict_percentage[i]/total_sum_letters * 100, 1)

    return dict_percentage




main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
x = get_count_char(main_str)
print(letter_percentage(x))