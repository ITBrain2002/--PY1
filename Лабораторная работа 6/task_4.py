import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        t = []
        for index, line in enumerate(f):
            z = line.strip(new_line).split(delimiter)
            if index == 0:
                headers = z
                continue
            t.append({})
            for i, _ in enumerate(headers):
                 t[-1][headers[i]] = z[i]
    return t

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))