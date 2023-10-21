# TODO  Напишите функцию count_letters
def count_letters(text):
    text_dictionary = {}
    for letter in text:
        if letter.isalpha():
            text_dictionary[letter] = text.count(letter)
    return text_dictionary


# TODO Напишите функцию calculate_frequency
def calculate_frequency(text_dictionary,length):
    for key,value in text_dictionary.items():
        text_dictionary[key] = value / length
    return text_dictionary


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

main_str = main_str.lower()
text_dictionary_ = count_letters(main_str)
text_dictionary_ = calculate_frequency(text_dictionary_, sum(text_dictionary_.values()))
for key, value in text_dictionary_.items():
    print(f"{key}: {value:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
