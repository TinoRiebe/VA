import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

engine = pyttsx3.init()
engine.say('Hallo Georg!!')
engine.runAndWait()

""" RATE"""
#rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)
"""VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
"""Saving Voice to a file"""
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()


wikipedia.set_lang('de')
client = wolframalpha.Client('3P5W7Y-Q5RPR73YQU')
# res = client.query('temperature in washington, DC on October 3, 2012')
# print(next(res.results).text)

sg.theme('DarkAmber')

layout = [[sg.Text('Guten Morgen Unwürdiger')],
          [sg.Text('Welche Frage hast Du?'), sg.InputText('weather rostock')],
          [sg.Button('Ok'), sg.Button('Cancel')]
          ]

window = sg.Window('Answer to everything', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

    try:
        res = client.query(values[0])
        text = next(res.results).text
        wolfram_res = 'Wolfram sagt:\n' + text
    except:
        wolfram_res = ("Wolfram kennt " + values[0] + ' nicht')

    try:
        wiki_res = 'Wikipedia sagt:\n ' + wikipedia.summary(values[0], sentences=2)
    except:
        wiki_res("Wikipedia kennt " + values[0] + ' nicht')

    answer = wolfram_res+ '\n\n' + wiki_res
    engine.say(wiki_res)
    sg.PopupNonBlocking(answer)
    #sg.popup(answer)
    engine.runAndWait()

window.close()

