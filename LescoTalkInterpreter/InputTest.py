from LexicAnalyzer import *
from SyntacticAnalyzer import parser

run = False
syntaxError = False
startCondition = '\m/'
sendList = ''

def transplant(list):
    temp = []

    for i in list:
        temp.append(i)

    return temp

def transplat_different_elements(donor, acceptor):
    temp = []
    for i in range(len(acceptor), len(donor)):
        temp.append(donor[i])

    return temp


while True:
    oldList = transplant(outputList)
    s = input(">> ")

    if s == startCondition:
        run = True
    else:
        continue

    while run:
        s1 = input(">< ")

        if s1 == startCondition:
            run = False
            break

        sendList += (s1 + ' ')

    try:
        parser.parse(sendList)

    except:
        print("Syntax Error")
        syntaxError = True


    sendList = ''

    finalList = transplat_different_elements(outputList, oldList)

    if not syntaxError:
        for j in finalList:
            print(j)
    else:
        print("Syntax Error!")