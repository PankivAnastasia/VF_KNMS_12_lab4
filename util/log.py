from datetime import datetime

is_log = False


def log(message):
    if is_log:
        print(message, " ", datetime.now())
