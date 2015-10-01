import datetime

def now_time_str():
    now = datetime.datetime.now()
    return now.strftime('%Y_%m_%d_%H_%M_%S')