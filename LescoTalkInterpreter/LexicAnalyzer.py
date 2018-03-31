import ply.lex as lex

tokens = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'EL', 'ELLA', 'USTED', 'USTEDES', 'NOSOTROS', 'ELLOS', 'ELLAS',
    'SANJOSE', 'ALAJUELA', 'CARTAGO', 'HEREDIA', 'PUNTARENAS', 'GUANACASTE', 'LIMON'
]

t_ignore = r' '

outputList = []

#  r'\b1011\.\b23[0-9]'
def t_A(t):
    r'\b1011\.\b23[0-9]5'
    global outputList
    outputList += ['A']
    return t

def t_B(t):
    r'\b1011\.\b22'
    global outputList
    outputList += ['B']
    return t

def t_0(t):
    r'\b0'
    global outputList
    outputList += ['0']
    return t

def t_1(t):
    r'\b1'
    global outputList
    outputList += ['1']
    return t

def t_2(t):
    r'\b2'
    global outputList
    outputList += ['2']
    return t

def t_3(t):
    r'\b3'
    global outputList
    outputList += ['3']
    return t

def t_4(t):
    r'\b4'
    global outputList
    outputList += ['4']
    return t

def t_5(t):
    r'\b5'
    global outputList
    outputList += ['5']
    return t

def t_6(t):
    r'\b6'
    global outputList
    outputList += ['6']
    return t

def t_7(t):
    r'\b7'
    global outputList
    outputList += ['7']
    return t

def t_8(t):
    r'\b8'
    global outputList
    outputList += ['8']
    return t

def t_9(t):
    r'\b9'
    global outputList
    outputList += ['9']
    return t

def t_error(t):
    global outputList
    print("Illegal Characters")
    outputList = []
    t.lexer.skip(1)

lex = lex.lex()

"""lex.input("1 0")

while True:
    tok = lex.token()

    if not tok:
        break

for h in outputList:
    print(h)"""
