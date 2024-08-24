# Import the required module for text 
# to speech conversion 
#REQUIRES INTERNET CONNECTION to do conversion

from gtts import gTTS 

# The text that you want to convert to audio 
mytext1 = "Its been 20 minutes, kindly look at somewhere 20 feet away for next 20 seconds"
# Language in which you want to convert 
language = 'en'
#Keep the length of the text below to be of maximum 100
#characters so that the audio finish playing during the 20 sec break
if len(mytext1)>100:
    print("""Keep the length of the text below to be of maximum 100 
    characters so that the audio finish playing during the 20 sec break""")
    exit()
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 

#Use line below for generating 20th minute alert audio
myobj = gTTS(text=mytext1, lang=language, slow=False)

# use line below for generating audio to alert for resuming work 
mytext2="You can now resume your work"
myobj2 = gTTS(text=mytext2, lang=language, slow=False) 

# Saving the converted audios in  mp3 files 

myobj.save("alarm.mp3") #give your path
myobj2.save("resume.mp3") 

#audio played the first time file is executed

mytext3="Don't forget to blink during the breaks"
myobj3 = gTTS(text=mytext3, lang=language, slow=False) 

myobj3.save("greeting.mp3")#your path


#Please note that everytime you run this script, and use the same names alarm,resume and greeting
#for the audio files, they will get replaced with the new converted audio files

