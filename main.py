from datetime import date
import data_dumper, json

NAME_OF_JSON_DICT = "dates"


current_date = date.today()


with open("pomo_data.json") as f:
    data = json.load(f)

print(data)
print(data.values())
