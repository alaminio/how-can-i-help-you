import webbrowser
import time
import os
from gtts import gTTS
import speech_recognition as sr

r = sr.Recognizer()
enable_voice_input = True

def hcihy():
    command = get_command('How can I help you?')
    do_it(command)
    time.sleep(1)


def get_command(msg = ''):
    notify(f'{msg}: ')
    if enable_voice_input is False:
        return input()

    with sr.Microphone() as source:
        audio = r.listen(source)
        return r.recognize_google(audio)

def notify(notice):
    language = get_land()
    audio = gTTS(text=notice, lang=language, slow=False)
    audio.save('notify.mp3')
    os.system("mpg321 notify.mp3") 
    print(notice)

def get_land():
    return 'en'

def visit_web(url):
    webbrowser.get().open(url)

def do_it(command):
    if 'exit' in command:
        exit()
    elif 'what is your name' in command:
        notify('My boss did not tell me yet')
    elif 'what time is it' in command:
        notify(time.ctime())
    elif 'search' in command:
        search = get_command('What do you want to search for?')
        visit_web(f'https://google.com/search?q={search}')
        notify('Here is what I found for ' + search)
    elif 'location' in command:
        location = get_command('What do you want to search for?')
        visit_web(f'https://google.nl/maps/place/{location}/&amp;')
        notify('Here is what I found for ' + location)
    elif 'visit' in command:
        search = get_command('What do you want to visit?')
        if 'ryansgo' in search:
            visit_web(f'https://ryansgo.com')
        elif 'ryanscomputer' in search:
            visit_web(f'https://ryanscomputer.com')
        else:
            visit_web(f'https://google.com/search?q={search}')

        notify('Here is what I found for ' + search)
    elif 'repeat' in command:
        talk = get_command('What do you want me to repeat?')
        notify(talk)
    else:
        notify("Sorry I did not get you")



if __name__ == '__main__':
    while True:
        hcihy()
