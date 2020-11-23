import schedule
import time
from playsound import playsound

def sound_alarm():
	playsound('E:/files/stdy/Useful Scripts/alarm.mp3')

def sound_resume_work_alert():
	playsound('E:/files/stdy/Useful Scripts/resume.mp3')



if __name__=="__main__":
	schedule.every(20).minutes.do(sound_alarm)
	schedule.every(20*60+20).seconds.do(sound_resume_work_alert)
	playsound('E:/files/stdy/Useful Scripts/greeting.mp3')
	while True:
		schedule.run_pending()
		time.sleep(1)