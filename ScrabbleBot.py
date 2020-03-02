"""Does the scrabble."""
import pyperclip

scrabble_dict = {
    'a':':a_scrabble:',
    'b':':b_scrabble:',
    'c':':c:',
    'd':':d:',
    'e':':e:',
    'f':':f:',
    'g':':g:',
    'h':':h:',
    'i':':i:',
    'j':':j:',
    'k':':k:',
    'l':':l:',
    'm':':m_scrabble:',
    'n':':n:',
    'o':':o_scrabble:',
    'p':':p:',
    'q':':q:',
    'r':':r:',
    's':':s:',
    't':':t:',
    'u':':u:',
    'v':':v_scrabble:',
    'w':':w:',
    'x':':x_scrabble:',
    'y':':y:',
    'z':':z:',
    ' ':':blank:',
    '!':':exclamation:',
    '?':':qblock:'
}

print(""" ____                 _     _     _      ____        _
/ ___|  ___ _ __ __ _| |__ | |__ | | ___| __ )  ___ | |_
\___ \ / __| '__/ _` | '_ \| '_ \| |/ _ \  _ \ / _ \| __|
 ___) | (__| | | (_| | |_) | |_) | |  __/ |_) | (_) | |_
|____/ \___|_|  \__,_|_.__/|_.__/|_|\___|____/ \___/ \__|
      

>>>====================Scrabble!======================<<<

""")

while True:
    letters = input("Give me your words: ")
    output = ''

    for letter in letters:
        try:
            output += scrabble_dict[letter.lower()]
        except:
            output += letter
    
    pyperclip.copy(output)
    print('\n\n')
    print('>>>>>===================<<<<<')
    print('>>>>>Copied to Clipboard<<<<<')
    print('>>>>>===================<<<<<')
    print('\n')
