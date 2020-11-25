import schedule
import time
import threading
from playsound import playsound

def sound_alarm():
	playsound('E:/files/stdy/Useful Scripts/eye_guard/alarm.mp3')#path to your file

def sound_resume_work_alert():
	playsound('E:/files/stdy/Useful Scripts/eye_guard/resume.mp3')#path to your file

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

if __name__=="__main__":
	playsound('E:/files/stdy/Useful Scripts/eye_guard/greeting.mp3') #path to your file
	schedule.every(20).minutes.do(run_threaded,sound_alarm)
	time.sleep(20)
	schedule.every(20).minutes.do(run_threaded,sound_resume_work_alert)
	
	while True:
		schedule.run_pending()
		time.sleep(1)