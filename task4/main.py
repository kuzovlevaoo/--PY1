import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE, output_file, new_line='/n', delimiter=',') -> list[dict]:
    with open(output_file, 'w', encoding='utf-8') as f_se:
        f_se.write('[' + new_line)
        first_row = True
        for i in csv_to_list_dict(INPUT_FILE):
            if not first_row:
                f_se.write(delimiter + new_line)
            f_se.write(indent + '{' + new_line)
            first_row = True
            for k, v in i.items():
                if not first_row:
                    f_se.write(delimiter + new_line)
                f_se.write(f'{indent}{indent}"{k}": {v}')
                first_row = False
            f_se.write(new_line + indent + '}')
            first_row = False
        f_se.write(new_line + ']')
        return csv_to_list_dict()


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
