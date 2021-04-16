import re

less_dic = {}
with open('text_6.txt', 'r', encoding="utf-8") as init_f:
    for i in init_f:
        lesson = i.split(':')[0]
        less_dic[lesson] = sum(list(map(int, re.sub(r'\D', ' ', i).split())))
print(less_dic)