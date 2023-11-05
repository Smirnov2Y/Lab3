# TODO Напишите функцию find_common_participants
def find_common_participants(participant1, participant2, comma = "," ):
    p1 = set(participant1.split(comma))
    p2 = set(participant2.split(comma))

    both = p1.intersection(p2)
    return sorted(list(both))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group))