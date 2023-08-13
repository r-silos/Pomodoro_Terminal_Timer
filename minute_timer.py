import time
import sys

# playsound allows us to play a sound file located in our computer in one line
from playsound import playsound

# total number of slots in prog bar that can be bars xor blank spaces
NUM_OF_PROG_SLOTS = 60


def timer(pomodoro_length=25, pomodoro_completed=0):
    """Timer function used to count down from default time of 25 minutes"""
    # total time is a constant used to calculate progress in prog bar
    TOTAL_TIME = pomodoro_length * 60
    # time in seconds used to count down total seconds to zero
    time_in_seconds = pomodoro_length * 60
    # time_until_next_bar used to calculate when can add bar to progress bar (there are 60 total SLOTS in prog bar)
    time_until_next_bar = int(time_in_seconds / NUM_OF_PROG_SLOTS)
    while time_in_seconds > -1:
        clear_terminal_text()
        minutes, seconds = divmod(time_in_seconds, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        # add space to left of string to make it appear in the mid
        timer_revised = timer.rjust(11)
        prog_bar = progress_bar(TOTAL_TIME, time_in_seconds, time_until_next_bar)
        prog_bar_revised = prog_bar.rjust(10)
        print(timer_revised, "\n", prog_bar_revised)

        # print(prog_bar, end="\r")
        time.sleep(1)
        time_in_seconds -= 1
    print("Pomodoro Done. You have completed {} pomodoros".format(pomodoro_completed))
    playsound(
        "C:\\Users\\Rsilo\Music\\audio_files\\pomodoro\\gameboy-advance-startup-sound-made-with-Voicemod-technology"
    )


def progress_bar(total_time, seconds_remaining, bar_time):
    """
    Python strings are immutable so will have to generate new progress bar on each iteration
    """
    if seconds_remaining == 0:
        return "[" + NUM_OF_PROG_SLOTS * "|" + "]"
    actual_prog_bars = (total_time - seconds_remaining) // bar_time
    num_of_white_spaces = NUM_OF_PROG_SLOTS - actual_prog_bars
    return "[" + "|" * actual_prog_bars + " " * num_of_white_spaces + "]"


def clear_terminal_text():
    # cursor up one line
    sys.stdout.write("\x1b[1A")

    # delete last line
    sys.stdout.write("\x1b[2K")

    # cursor up one line
    sys.stdout.write("\x1b[1A")

    # delete last line
    sys.stdout.write("\x1b[2K")


timer(1)
# To DO: fix error with playsound as error message says "ModuleNotFoundError: No module named 'playsound'"
