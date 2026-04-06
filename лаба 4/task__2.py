import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    file = open(INPUT_FILENAME, 'r', encoding='utf-8')
    content = file.read()
    file.close()

    lines = content.split('\n')

    while lines and lines[-1] == '':
        lines.pop()

    headers = lines[0].split(',')

    result = []

    for i in range(1, len(lines)):
        line = lines[i]
        values = line.split(',')

        record = {}
        for j in range(len(headers)):
            if j < len(values):
                record[headers[j]] = values[j]
            else:
                record[headers[j]] = ""

        result.append(record)

    out_file = open(OUTPUT_FILENAME, 'w', encoding='utf-8')
    json.dump(result, out_file, indent=4, ensure_ascii=False)
    out_file.close()


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')