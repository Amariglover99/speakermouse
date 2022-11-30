import speech_recognition as sr
import pyautogui


# get audio from the microphone
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Speak:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        txt = r.recognize_google(audio)

        print(">>" + txt)
        # prints the desired commands
        if txt == 'click':
            print('click')
            pyautogui.doubleClick()
        elif txt == 'right':
            print('go right!!')
            pyautogui.move(300, 0)
        elif txt == 'left' or txt == 'lift':
            print('go left!!')
            pyautogui.move(-300, 0)
        elif txt == 'up':
            print('go up!!')
            pyautogui.move(0, -300)
        elif txt == 'down' or 'go down':
            print('go down!!')
            pyautogui.move(0, 300)
    # prints if only the program doesn't understand what the user is saying
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
