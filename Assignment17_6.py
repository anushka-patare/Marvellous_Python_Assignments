import schedule
import time

def MySchedule1():
    print("Lunch Time! Its a 1 PM")

def MySchedule2():
    print("Wrap up work.Its a 6PM")

def main():
    schedule.every().day.at("01:00:00").do(MySchedule1)
    schedule.every().day.at("06:00:00").do(MySchedule2)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()