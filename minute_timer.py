import time


def timer(pomodoro_length=25):
    """Timer function used to count down from default time of 25 minutes"""
    print("test")
    # time in seconds used to count down total seconds to zero
    time_in_seconds = pomodoro_length * 60
    while time_in_seconds > 0:
        minutes, seconds = divmod(time_in_seconds, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        prog_bar = progress_bar(pomodoro_length, time_in_seconds)
        print(timer, end="\r")
        print(prog_bar, end="\r")
        time.sleep(1)
        time_in_seconds -= 1
    print("time is up")


def progress_bar(total_time, seconds_remaining):
    # full_bar = "[" + "|" * 80 + "]"
    # have to call int() to get whole number after division/multiplication
    total_seconds = total_time * 60
    num_of_bars = 80 * (abs(total_seconds / abs((total_seconds / seconds_remaining))))
    numb_of_white_space = 80 - num_of_bars
    bar = "[" + num_of_bars * "|" + numb_of_white_space * " " + "]"
    return bar


timer()
