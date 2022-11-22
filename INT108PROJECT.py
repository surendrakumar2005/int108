import speech_recognition as sr
import pyttsx3
import  pywhatkit
import  datetime
import  wikipedia
import pyjokes
listener=sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(te):
    engine.say(te)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('🎙️...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command
def game():
    from random import shuffle
    my_list = [" ", "O", " "]
    def shuff(my_list):
        shuffle(my_list)
        return my_list
    def player_guess():
        guess = ''
        while guess not in ['0', '1', '2']:
            guess = input('Enter your Guess(0,1,2): ')
        return int(guess)
    def result(my_list, player_guess):
        if my_list[player_guess] == 'O':
            print("You Won!!")
        else:
            print("Better Luck Next Time")
            print(my_list)
    a = shuff(my_list)
    b = player_guess()
    result(a, b)
def run():
    command=take_command()
    if 'play' in command:
        video = command.replace('play', '')
        print(f'playing {video}')
        speak(f'playing {video}')
        pywhatkit.playonyt(video)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M  %p')
        print(f"time is {time}")
        speak(f"time is {time}")
    elif 'wikipedia' in command:
        command= command.replace('wikipedia','')
        result=wikipedia.summary(command, 2)
        print(result)
        speak(result)
    elif 'game' in command:
        game()
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        speak(joke)
        print(joke)
    elif 'hi' in command:
        print("HI")
        speak("HI")
    elif 'hello' in command:
        print('HELLO')
        speak('hello')
    elif 'how are you' in command:
        print('I Am Great. What about you?')
        speak('I Am Great. What about you')
    elif 'how old are you' in command:
        print('I Am two years older then you')
        speak('I Am two years older then you')
    else:
        print(command)
        speak(command)
        pywhatkit.search(command)
run()
