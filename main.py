import wolframalpha
import PySimpleGUI as sg
import wikipedia
wikipedia.set_lang('de')
client = wolframalpha.Client('3P5W7Y-Q5RPR73YQU')
res = client.query('temperature in washington, DC on October 3, 2012')
#print(next(res.results).text)

sg.theme('DarkAmber')

layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter your question'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]
          ]

window = sg.Window('Window title', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wolfram_res = client.query(values[0])
        answer = 'Wolfram said: ' + next(wolfram_res.results).text
        sg.Popup(answer)
    except:
        sg.Popup("Wolfram doesnt know anything about " + values[0])
    try:
        wiki_res = wikipedia.summary(values[0], sentences=1)
        answer = 'Wikipedia sagt: ' + wiki_res
        sg.popup(answer)
    except:
        sg.Popup("Wikipedia doesnt know anything about " + values[0])
window.close()

