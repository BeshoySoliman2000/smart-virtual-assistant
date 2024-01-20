import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui
import openai
import time
import wikipedia
import webbrowser

#put your vhat gpt api_key here
openai.api_key = ""

messages = [ {"role": "system", "content":
              "You are a intelligent assistant."} ]




def talk(Text):
    Speaking_object = pyttsx3.init()
    voices = Speaking_object.getProperty('voices')
    Speaking_object.setProperty('voice', voices[0].id)
    Speaking_object.say(Text)
    Speaking_object.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        # r.pause_threshold = 0.1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # english we can also use 'hi-In'
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            talk("Say that again sir")
            return "None"

        return Query


def tellDay():
    x = datetime.datetime.now()
    Date = x.strftime("%A\n %d of %B \n%Y")
    talk("The day is " + Date)

def tellTime():
    x = datetime.datetime.now()
    Time = x.strftime("%I%p%M Minutes")
    talk("The Time is " + Time)

def WelcomeMessage():
    talk("Hello Sir I'm jack\n your Desktop Assistant \n how can i help you")
def Talk_ChatGPT(Talking):
    message = Talking
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    talk(f"ChatGPT Says: {reply}")
    messages.append({"role": "assistant", "content": reply})

def Virtual_AssistantQuery():
    Vquery = takeCommand().lower()
    if "jack" in Vquery:
        WelcomeMessage()
        while True:
            Vquery = takeCommand().lower()
            if "thanks jack" in Vquery or "thank you jack" in Vquery:
                talk(f"You're welcome sir")
                break
            elif "from chatgpt" in Vquery or "from chat gpt" in Vquery or "chatgpt" in Vquery or "from ai"in Vquery:
                talk(f"Checking Chat gpt")
                Vquery = Vquery.replace("chatgpt","")
                Talk_ChatGPT(Vquery)
            elif "from wikipedia" in Vquery:

                talk("Checking the wikipedia ")
                query = Vquery.replace("wikipedia", "")

                result = wikipedia.summary(query, sentences=4)
                talk("According to wikipedia")
                talk(result)
            elif "bye" in Vquery:
                talk("Bye. Check Out GFG for more exciting things")
                break
            elif "which day it is" in Vquery:
                tellDay()
                continue

            elif "tell me the time" in Vquery or "what is the time" in Vquery:
                tellTime()
                continue
            elif "maps" in Vquery or "position" in Vquery:
                talk("where do you want to go")
                place = takeCommand().lower()
                url = 'https://www.google.nl/maps/search/' + place
                webbrowser.get().open(url)
                talk("Here is the map of " + place)
            elif 'search' in Vquery or 'the search' in Vquery:
                talk("what's in your mind")
                search = takeCommand().lower()
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                talk('I finished' + search)
            elif "open the camera"in Vquery or 'open camera' in Vquery:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('camera')
                time.sleep(1)
                pyautogui.hotkey('enter')
            elif "open the calculator"in Vquery or 'open calculator' in Vquery:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('calculator')
                time.sleep(1)
                pyautogui.hotkey('enter')
            elif "tell me a joke" in Vquery:
                Talk_ChatGPT("tell me a joke")
            elif "i'm sad" in Vquery:
                Talk_ChatGPT("i'm sad")


while True:
    Virtual_AssistantQuery()
    # Text = takeCommand()
    # Talk_ChatGPT(Text)
# while True:
    # WelcomeMessage()
    # # Tex = takeCommand()
    # # talk(Tex)
# query = f"i need some information about the middle east"
#
#     # it will give the summary of 4 lines from
#     # wikipedia we can increase and decrease
#     # it also.
# result = wikipedia.summary(query, sentences=4)
# print(result)