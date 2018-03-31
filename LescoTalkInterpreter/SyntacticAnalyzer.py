import ply.yacc as yacc
from LexicAnalyzer import *

def p_program(p):
    '''program : block'''
    print("Program")

def p_block(p):
    '''block : word'''
    print("Block")

"""def p_sentence(p):
    '''sentence : letter'''
    print("Sentence")"""

def p_word(p):
    '''word : letter
            | number
            | pronoun
            | province'''

    print("Word")

def p_letter(p):
    '''letter : A
              | B
    '''
    print("Letter")

def p_number(p):
    '''number : 1
              | 2
              | 3
              | 4
              | 5
              | 6
              | 7
              | 8
              | 9'''
    print("Number")

def p_pronoun(p):
    '''pronoun : EL
               | ELLA
               | USTED
               | USTEDES
               | NOSOTROS
               | ELLOS
               | ELLAS'''
    print("Pronoun")

def p_province(p):
    '''province : SANJOSE
                | ALAJUELA
                | CARTAGO
                | HEREDIA
                | PUNTARENAS
                | GUANACASTE
                | LIMON'''

def p_error(p):
    print("Syntax Error Found!" + p)

parser = yacc.yacc()

while True:
    try:
        s = input(">> ")

    except EOFError:
        break

    try:
        parser.parse(s)
        for h in outputList:
            print(h)

    except:
        print("Syntax Error")
