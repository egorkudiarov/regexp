from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

pattern =  r'^(\+7|8)[\s]?[(]?(\d{3})[)]?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})[\s]?[(\s]?(доб\. \d+|)'
phone_code = re.compile(pattern)
blank = [' ' for i in range(len(contacts_list[0]))]

header, contacts_list = contacts_list[0], contacts_list[1:]

def func(x, y):
    if x == '':
        x = y
    return x

for x, y in zip(contacts_list[0], contacts_list[1]):
    print(func(x, y))


for num, line in enumerate(contacts_list):
    lfs = line[0].split(' ') 
    fs = line[1].split(' ')
    match (len(lfs), len(fs)):
        case (3, 1):
            line[0], line[1], line[2] = lfs
        case (2, 1):
            line[0], line[1] = lfs
        case (1, 2):
            line[1], line[2] = fs
    result = phone_code.search(line[5])
    if result != None:
        line[5] = f'+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)} {result.group(6)}'
    for check_num, check_line in enumerate(contacts_list[:num]):
        if line[0] == check_line[0] and line[1] == check_line[1] and ((line[2] == check_line[2]) or (line[2] == '' and check_line[2] != '') or (line[2] != '' and check_line[2] == '')):
            contacts_list[check_num] = list(map(func, contacts_list[check_num], line))
            contacts_list[num] = blank.copy()

for _ in range(contacts_list.count(blank)):
    contacts_list.remove(blank)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)