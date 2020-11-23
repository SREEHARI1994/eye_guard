# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
#import os 

# The text that you want to convert to audio 
#mytext = 'Welcome to ThingQbator, Hashim Abdulla'
mytext1 = "Its been 20 minutes, kindly look at somewhere 20 feet away for next 20 seconds"
# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 

#Use line below for generating 20 minute alert audio
myobj = gTTS(text=mytext1, lang=language, slow=False)
mytext2="You can now resume your work"
# use line below for generating audio to alert for resuming work 
myobj2 = gTTS(text=mytext2, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("E:/files/stdy/Useful Scripts/alarm.mp3") 
myobj2.save("E:/files/stdy/Useful Scripts/resume.mp3") 

#audio played the first time file is executed

mytext3="Don't forget to blink during the breaks"
myobj3 = gTTS(text=mytext3, lang=language, slow=False) 

myobj3.save("E:/files/stdy/Useful Scripts/greeting.mp3")

# Playing the converted file 
#os.system("tm.mp3") 
