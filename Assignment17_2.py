import schedule
import datetime
import time


def MySchedule():
    print("The current time is:",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()