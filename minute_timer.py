import time
import sys
from colorama import just_fix_windows_console
import winsound

# total number of slots in prog bar that can be bars xor blank spaces
NUM_OF_PROG_SLOTS = 60


def timer(pomodoro_length=25, pomodoro_completed=0):
    """Timer function used to count down from default time of 25 minutes"""

    # MAX_TIME is a constant used keep track of total amt of time timer runs for
    MAX_TIME = pomodoro_length * 60

    # TIME_UNTIL_NEXT_BAR used to calculate when can add bar to progress bar (there are 60 total SLOTS in prog bar)
    TIME_UNTIL_NEXT_BAR = int(MAX_TIME / NUM_OF_PROG_SLOTS)

    # time in seconds used to count down total seconds to zero
    time_countdown = pomodoro_length * 60

    while time_countdown > -1:
        clear_terminal_text()
        minutes, seconds = divmod(time_countdown, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        timer_revised = timer.center(120, " ")
        prog_bar = progress_bar(MAX_TIME, time_countdown, TIME_UNTIL_NEXT_BAR)
        prog_bar_revised = prog_bar.center(120, " ")
        print(timer_revised, "\n", prog_bar_revised)

        # print(prog_bar, end="\r")
        time.sleep(1)
        time_countdown -= 1
    winsound.PlaySound("gba_noise.wav", 0)
    print("Pomodoro Done. You have completed {} pomodoros".format(pomodoro_completed))


def progress_bar(total_time, seconds_remaining, bar_time):
    """
    Python strings are immutable so will have to generate new progress bar on each iteration
    """
    if seconds_remaining == 0:
        return "[" + NUM_OF_PROG_SLOTS * "|" + "]"
    actual_prog_bars = (total_time - seconds_remaining) // bar_time
    num_of_white_spaces = NUM_OF_PROG_SLOTS - actual_prog_bars
    return "[" + "|" * actual_prog_bars + " " * num_of_white_spaces + "]"


def clear_terminal_text(lines_to_clear=2):
    for _ in range(0, lines_to_clear):
        # cursor up one line
        sys.stdout.write("\x1b[1A")
        # delete last line
        sys.stdout.write("\x1b[2K")


def main():
    just_fix_windows_console()
    timer(1)


main()
