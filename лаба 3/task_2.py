def find_common_participants(group1: str, group2: str, delimiter: str = ",") -> list:
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)
    common = set(participants1) & set(participants2)
    return sorted(common)

# Проверка работы
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(result)  # ['Петров', 'Сидоров']