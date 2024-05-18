import schedule
import time

def schedule_job(job_function):
    schedule.every().day.at("09:00").do(job_function)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
