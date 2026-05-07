import json

def load_records():
    
    try:
        with open("cigarette_data.json", "r") as file:
            records = json.load(file)

    except FileNotFoundError:
        records = []

    return records


def save_records(records):

    with open("cigarette_data.json", "w") as file:
        json.dump(records, file, indent=4)