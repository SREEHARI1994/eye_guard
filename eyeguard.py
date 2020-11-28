import schedule
import time
import threading
from playsound import playsound
import sys

minutes=20
seconds=20
if len(sys.argv)==3:
	if int(sys.argv[2])>seconds:
		seconds=int(sys.argv[2])
	if int(sys.argv[1])>2:
		minutes=int(sys.argv[1])
	else:
		minutes=2
	
elif len(sys.argv)==2:
	if int(sys.argv[1])>2:
		minutes=int(sys.argv[1])
	else:
		minutes=2

def sound_alarm():
	playsound('E:/files/stdy/Useful Scripts/eye_guard/alarm.mp3')#path to your file

def sound_resume_work_alert():
	playsound('E:/files/stdy/Useful Scripts/eye_guard/resume.mp3')#path to your file

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

if __name__=="__main__":
	playsound('E:/files/stdy/Useful Scripts/eye_guard/greeting.mp3') #path to your fil
	schedule.every(minutes).minutes.do(run_threaded,sound_alarm)
	time.sleep(seconds)
	schedule.every(minutes).minutes.do(run_threaded,sound_resume_work_alert)
	while True:
		schedule.run_pending()
		time.sleep(1)