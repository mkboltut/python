import json
profit = {}
average = {}
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, form, earning, expend = line.split()
        profit[name] = int(earning) - int(expend)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
    average = {'average_profit': round(prof_aver)}
list_to_json = [profit, average]
with open('file_7.json', 'w', encoding="utf-8") as write_js:
    json.dump(list_to_json, write_js, sort_keys=False, indent=4, ensure_ascii=False)
