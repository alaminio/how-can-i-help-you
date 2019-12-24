import webbrowser
import time
import os
from gtts import gTTS


def main():
    command = get_command()
    do_it(command)


def get_command(msg = False):
    if msg:
        return input(f'{msg}: ')
    return input('How can I help you?: ')

def notify(notice):
    language = get_land()
    print(notice)
    audio = gTTS(text=notice, lang=language, slow=False)
    audio.save('notify.mp3')
    os.system("mpg321 notify.mp3") 

def get_land():
    return 'en'

def visit_web(url):
    webbrowser.get().open(url)

def do_it(command):
    if 'exit' in command:
        exit()
    if 'what is your name' in command:
        notify('My boss did not tell me yet')
    if 'what time is it' in command:
        notify(time.ctime())
    if 'search' in command:
        search = get_command('What do you want to search for?')
        visit_web(f'https://google.com/search?q={search}')
        notify('Here is what I found for ' + search)
    if 'location' in command:
        location = get_command('What do you want to search for?')
        visit_web(f'https://google.nl/maps/place/{location}/&amp;')
        notify('Here is what I found for ' + location)
    if 'visit' in command:
        search = get_command('What do you want to visit?')
        if 'ryansgo' in search:
            visit_web(f'https://ryansgo.com')
        if 'ryanscomputer' in search:
            visit_web(f'https://ryanscomputer.com')

        notify('Here is what I found for ' + search)
    if 'repeat' in command:
        talk = get_command('What do you want me to repeat?')
        notify(talk)



if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)