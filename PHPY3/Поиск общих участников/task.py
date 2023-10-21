def find_common_participants(participants_first, participants_second, sep=","):
    participants_first = participants_first.split(sep)
    participants_second = participants_second.split(sep)
    result = set(participants_first).intersection(participants_second)
    return sorted(list(result))





participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep="|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
