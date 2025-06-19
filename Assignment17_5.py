import schedule
import time

def MySchedule():
    timestamp=time.ctime()

    FileName="Marvellous.txt"
    fobj=open(FileName,"w")
    
    fobj.write(timestamp)

def main():
    schedule.every(5).minutes.do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()

    