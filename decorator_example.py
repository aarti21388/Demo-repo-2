import time
from datetime import datetime

def log_datetime_decorator(func):
    ''' Log datatime of the function'''
    def wrapper_func():
        print(f"Function:{func.__name__}")
        print(f"Execute on {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=========================")
        return func()
    return wrapper_func


@log_datetime_decorator
def daily_cron_job():
    time.sleep(6)
    print("daily cron job has finiched")

@log_datetime_decorator
def weekly_cron_job():
    time.sleep(60)
    print("Weekly cron job has finiched")

daily_cron_job()
weekly_cron_job()

#output:
# Function:daily_cron_job
# Execute on 2022-12-02 10:53:08
# =========================
# daily cron job has finiched
# Function:weekly_cron_job
# Execute on 2022-12-02 10:53:14
# =========================
# Weekly cron job has finiched
