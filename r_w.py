# Задание 1
from pprint import pprint
import os

file_name = "recipes.txt"


def сooking(file_name):
    with open(file_name, encoding="utf-8") as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients = []
            ingredients_dict = {'ingredient_name': 1, 'quantity': 1, 'measure': 1}
            for item in range(int(file.readline())):
                ingredient = file.readline().strip().split('|')
                ingredients_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1],
                                    'measure': ingredient[2]}
                ingredients.append(ingredients_dict)
            cook_book[dish] = ingredients
            file.readline()
        return cook_book


print()
pprint(f"cook_book = {сooking(file_name)}")
print()


# Задание 2

# Функция подсчета повторов блюд


def repetition_сount(dishes):
    repetition_dict = {}
    count = 1
    for dish in dishes:
        if dish in repetition_dict.keys():
            repetition_dict[dish] += 1
        else:
            repetition_dict.setdefault(dish, 1)

    for num_repeat in list(repetition_dict.values()):
        count *= num_repeat
    return count


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict1 = {}  # промежуточный словарь. Нужен для создания основного
    ingredients_dict2 = {}  # основной словарь

    for dish, ingredients in сooking(file_name).items():
        if dish in dishes:
            for meaning in ingredients:
                ingredients_list = []
                for view, position in meaning.items():
                    ingredients_list.append([view, position])
                ingredients_list[1], ingredients_list[2] = ingredients_list[2], ingredients_list[1]
                ingredients_dict1 = {ingredients_list[0][1]: {ingredients_list[1][0]: ingredients_list[1][1],
                                                              ingredients_list[2][0]: int(ingredients_list[2][1])
                                                                                      * person_count * repetition_сount(
                                                                  dishes)}}
                ingredients_dict2.update(ingredients_dict1)
    return (ingredients_dict2)


pprint(get_shop_list_by_dishes(['Омлет'], 1))

# Задание 3
catalog = "sorted"
file_name1 = "1.txt"
file_name2 = "2.txt"
file_name3 = "3.txt"
file_result = "result.txt"
base_path = os.getcwd()
full_path1 = os.path.join(base_path, catalog, file_name1)
full_path2 = os.path.join(base_path, catalog, file_name2)
full_path3 = os.path.join(base_path, catalog, file_name3)
file_name_list = [full_path1, full_path2, full_path3]
full_path_result = os.path.join(base_path, catalog, file_result)


def reading(file_name_list):
    read_dict = {}
    sorted_dict = {}
    for full_path in file_name_list:
        with open(full_path, encoding="utf-8") as file:
            lines = file.readlines()
            # full_path[-5:]
            # len(lines)
            count = 0
            value_list = []
            for line in lines:
                count += 1
                # f"Строка номер {count} файла номер {full_path[-5]}"
                value_list.append(f"Строка номер {count} файла номер {full_path[-5]}")
            read_dict[full_path[-5:]] = (len(lines), value_list)
# сортировка
    sorted_keys = sorted(read_dict, key=read_dict.get)
    for val_dict in sorted_keys:
        sorted_dict[val_dict] = read_dict[val_dict]
    return sorted_dict


reading(file_name_list)


def writing(full_path_result, mode, data):
    for key_dict, value_dict in reading(file_name_list).items():
        with open(full_path_result, "a", encoding="utf-8") as file:
            file.write(f"\n{key_dict} \n{list(value_dict)[0]} \n{ ' '.join(list(value_dict)[1])}\n ")


writing(full_path_result, "a", reading(file_name_list))


