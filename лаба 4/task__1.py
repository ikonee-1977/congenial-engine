import json

def task():
    f = open("input.json", "r", encoding="utf-8")
    data = json.load(f)
    f.close()

    total = 0.0

    for i in range(len(data)):
        score = data[i]["score"]
        weight = data[i]["weight"]
        total = total + score * weight

    return round(total, 3)

print(task())