# this function will be used to create a data entry in json file
def pomodoro_day_data(
    date,
    num_of_pomodoros=0,
):
    nested_dictionary = {}
    nested_dictionary[date] = {}
    nested_dictionary[date]["pomodoros completed"] = num_of_pomodoros
    nested_dictionary[date]["time worked"] = (
        nested_dictionary[date]["pomodoros completed"] * 25
    )
    return nested_dictionary
