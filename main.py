from json.tool import main
import PySimpleGUI as sg
import json

C_ROMAN = 0
C_MANGA = 1
C_BD = 2
C_COMICS = 3

f = open('data.json','r')
data = json.load(f)
f.close()
sg.theme('DarkAmber')   # Add a touch of color
layoutMain = [ 
        [ sg.InputText(key='NewBookInput') ],
        [sg.Radio('Roman', "RADIO1", default=True,key="radioRoman"), sg.Radio('Manga', "RADIO1",key="radioManga"), sg.Radio('BD', "RADIO1",key="radioBD"),sg.Radio('Comics', "RADIO1",key="radioComics"),
        sg.Button('Ajouter')],
        [ sg.InputText(),sg.Button('Recherche')],
        [sg.Listbox(values = [], select_mode=sg.SELECT_MODE_EXTENDED,enable_events=True, size=(50,20), bind_return_key=True, key='listOfBook')],
        ]

window = sg.Window('Window Title', layoutMain)

def writeFile():
    f = open('data.json','w+')
    f.write(json.dumps(data))
    f.close()

def getValFromConst(param):
    val = C_ROMAN
    if param['radioManga']:
        val = C_MANGA
    elif param['radioBD']:
        val = C_BD
    elif param['radioComics']:
        val = C_COMICS
    return val

def open_window(value):
    val = value.split('|')
    layoutChild = [
        [ sg.InputText(val[1],key='BookTitle') ],
        [sg.Radio('Roman', "RADIO1", default= (val[0].find('Roman')!=-1),key="radioRoman"), 
         sg.Radio('Manga', "RADIO1",key="radioManga",default= (val[0].find('Manga')!=-1)), 
         sg.Radio('BD', "RADIO1",key="radioBD",default= (val[0].find('BD')!=-1)),
         sg.Radio('Comics', "RADIO1",key="radioComics",default= (val[0].find('Comics')!=-1))],
         [sg.InputText(val[2],key='Numeros')],
         [sg.Button('Update')]
    ]
    window = sg.Window("Second Window", layoutChild, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == 'Update':
            for book in data:
                if val[1].find(book['title']) != -1:
                    book['title'] = values['BookTitle'].strip()
                    radio = getValFromConst(values)
                    book['type'] = radio
                    book['numeros'] = values['Numeros'].strip()
                    writeFile()
            break
    window.close()

lastSearch = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Recherche":
        val=[]
        lastSearch = values[0]
        for book in data:
            if book["title"].find(values[0]) != -1:
                typeOfBook = "Roman "
                if book['type'] == C_MANGA:
                    typeOfBook = "Manga "
                elif book['type'] == C_BD : 
                    typeOfBook = 'BD    '
                elif book['type'] == C_COMICS:
                    typeOfBook = 'Comics'
                val.append(typeOfBook + " | " + book["title"] + " | " + book["numeros"])
        window['listOfBook'].update(val)
    elif event == "Ajouter":
        typeOfBook = getValFromConst(values)
        val = {
            "title" : values['NewBookInput'],
            "type"  : typeOfBook,
            "numeros" : ""
        }
        data.append(val)
        writeFile()
        window['NewBookInput'].update('')
    elif event =='listOfBook':
        open_window(values['listOfBook'][0])
        val=[]
        for book in data:
            if book["title"].find(lastSearch) != -1:
                typeOfBook = "Roman "
                if book['type'] == C_MANGA:
                    typeOfBook = "Manga "
                elif book['type'] == C_BD : 
                    typeOfBook = 'BD    '
                elif book['type'] == C_COMICS:
                    typeOfBook = 'Comics'
                val.append(typeOfBook + " | " + book["title"] + " | " + book["numeros"])
        window['listOfBook'].update(val)

window.close()