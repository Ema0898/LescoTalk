import cv2
import numpy as np
from csv_managment import comparate_with_database
import socket

adress = '0.0.0.0'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((adress, port))
sock.listen(1)

connections = []
withAndroid = 0

finger_position_list = [[], []]

counter = 0
salidaFinal = ""
isSend = False
mensaje = ""
database_name = 'letras.csv'
msg_to_show = ""
x1, y1, x2, y2 = 0,0,0,0


def string(vec):
    result = ""
    for i in vec:
        result += str(i) + "!"

    return result

def send(message):
    for connection in connections:
        connection.send(bytes(message + "\n", 'utf-8'))

if (withAndroid):
    print("Waiting for connections")
    while True:
        client, a = sock.accept()
        connections.append(client)
        send("hola")
        break

    print("Connected")
    print(connections)

cap = cv2.VideoCapture(0)


muestras = 0
vecmin , vecmax = [999,999,999] , [0,0,0]
mousex , mousey = -1,-1
red_lower, red_upper , blue_lower , blue_upper, green_lower , green_upper , purple_lower = 0,0,0,0,0,0,0
purple_upper ,yellow_lower , yellow_upper , orange_lower , orange_upper , black_lower , black_upper = 0,0,0,0,0,0,0


def mouseclic(event,x,y,flags,param):
    global muestras , vecmax , vecmin
    global red_lower, red_upper , blue_lower , blue_upper, green_lower , green_upper , purple_lower
    global purple_upper ,yellow_lower , yellow_upper , orange_lower , orange_upper , black_lower , black_upper
    if event == cv2.EVENT_LBUTTONUP:
        pixelbrg = img3[y,x]
        pixelnp = np.uint8([ [ pixelbrg ] ] )
        pixelhsv = cv2.cvtColor(pixelnp,cv2.COLOR_BGR2HSV)
        pixelvec = pixelhsv[0][0]
        print(pixelvec)
        if (pixelvec[0] >= vecmax[0]):
            vecmax[0] = pixelvec[0] 
        if (pixelvec[1] >= vecmax[1]):
            vecmax[1] = pixelvec[1] 
        if (pixelvec[2] >= vecmax[2]):
            vecmax[2] = pixelvec[2] 
        if (pixelvec[0] <= vecmin[0]):
            vecmin[0] = pixelvec[0] 
        if (pixelvec[1] <= vecmin[1]):
            vecmin[1] = pixelvec[1] 
        if (pixelvec[2] <= vecmin[2]):
            vecmin[2] = pixelvec[2] 
        #print(vecmin,' - ',vecmax)
        muestras +=1
        
        if muestras == 3:
            blue_lower = np.array(vecmin, np.uint8)
            blue_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(blue_lower, ' - ',blue_upper)     
        if muestras == 6:
            purple_lower = np.array(vecmin, np.uint8)
            purple_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(purple_lower, ' - ',purple_upper) 
        if muestras == 9:
            red_lower = np.array(vecmin, np.uint8)
            red_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(red_lower, ' - ',red_upper)       
        if muestras == 12:
            green_lower = np.array(vecmin, np.uint8)
            green_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(green_lower, ' - ',green_upper)   
        if muestras == 15:
            yellow_lower = np.array(vecmin, np.uint8)
            yellow_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(yellow_lower, ' - ',yellow_upper) 
        if muestras == 18:
            black_lower = np.array(vecmin, np.uint8)
            black_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(black_lower, ' - ',black_upper)   
        if muestras == 21:
            orange_lower = np.array(vecmin, np.uint8)
            orange_upper = np.array(vecmax, np.uint8)
            vecmin = [999,999,999] 
            vecmax = [0,0,0]
            print(orange_lower, ' - ',orange_upper) 


tiempo = 0
_, img3 = cap.read()

while (cap.isOpened()):
    _, img3 = cap.read()
    cv2.imshow("Calibration", img3)
    cv2.moveWindow("Calibration", 0, 0)
    cv2.setMouseCallback('Calibration',mouseclic)

    k = cv2.waitKey(10)
    if k == 27:
        cv2.destroyWindow("Calibration")
        break
    if k == 49:
        muestras = 0
    if k == 50:
        muestras = 3
    if k == 51:
        muestras = 6
    if k == 52:
        muestras = 9
    if k == 53:
        muestras = 12
    if k == 54:
        muestras = 15

tiempo = 0
_, img4 = cap.read()
#for t in range(10):
while (cap.isOpened()):
    if tiempo < 10:
        _, img4 = cap.read()
    cv2.imshow("Calibration2", img4)
    cv2.moveWindow("Calibration2", 0, 0)
    cv2.setMouseCallback('Calibration2',mouseclic)
    tiempo +=1
    k = cv2.waitKey(10)
    if k == 27:
        break
    if k == 55:
        muestras = 18

#red
red_lower = np.array([172, 140, 100], np.uint8)
red_upper = np.array([180, 182, 205], np.uint8)

# defining the range of blue color
blue_lower = np.array([104, 100, 85], np.uint8)
blue_upper = np.array([118, 206, 175], np.uint8)

# defining the range of yellow color
yellow_lower = np.array([25, 125, 100], np.uint8)
yellow_upper = np.array([30, 160, 200], np.uint8)

# defining the range of purple color
purple_lower = np.array([117, 75, 60], np.uint8)
purple_upper = np.array([123, 113, 170], np.uint8)

# defining the range of green color
green_lower = np.array([39, 69, 100], np.uint8)
green_upper = np.array([45, 155, 210], np.uint8)

# defining the range of black color
black_lower = np.array([70, 0, 0], np.uint8)
black_upper = np.array([100, 60, 80], np.uint8)

orange_lower = np.array([3, 90, 120], np.uint8)
orange_upper = np.array([15, 170, 239], np.uint8)
'''
while (cap.isOpened()):
    cv2.imshow("Calibration2", img4)
    cv2.moveWindow("Calibration2", 0, 0)
    

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyWindow("Calibration2")
        break
'''
dev = 0
while (cap.isOpened()):
    _, frame = cap.read()

    # converting frame (img2 i.e BGR) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    horizontal = 0
    vertical = 0
    

    # finding the range of red,blue and yellow color in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    purple = cv2.inRange(hsv, purple_lower, purple_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)
    black = cv2.inRange(hsv, black_lower, black_upper)
    orange = cv2.inRange(hsv, orange_lower, orange_upper)

    #Morphological transformation, Dillation
    red = cv2.threshold(red, 25, 255, cv2.THRESH_BINARY)[1]
    red = cv2.dilate(red, None, iterations=2)

    blue = cv2.threshold(blue, 25, 255, cv2.THRESH_BINARY)[1]
    blue = cv2.dilate(blue, None, iterations=2)
    
    yellow = cv2.threshold(yellow, 25, 255, cv2.THRESH_BINARY)[1]
    yellow = cv2.dilate(yellow, None, iterations=2)
    
    purple = cv2.threshold(purple, 25, 255, cv2.THRESH_BINARY)[1]
    purple = cv2.dilate(purple, None, iterations=2)
    
    green = cv2.threshold(green, 25, 255, cv2.THRESH_BINARY)[1]
    green = cv2.dilate(green, None, iterations=2)
    
    black = cv2.threshold(black, 25, 255, cv2.THRESH_BINARY)[1]
    black = cv2.dilate(black, None, iterations=2)

    orange = cv2.threshold(orange, 25, 255, cv2.THRESH_BINARY)[1]
    orange = cv2.dilate(orange, None, iterations=2)

    red_objects, blue_objects, yellow_objects, green_objects, orange_objects, purple_objects, black_objects = [], [], [], [], [], [], []

    #Tracking the Red Color
 
    contornosimg = red.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xr = 0
    yr = 0
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            red_objects.append([x+w/2 , y+h/2])
            cv2.putText(frame,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))
            xr = x
            yr = y
        
    contornosimg = blue.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xb = 0
    yb = 0
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x +w, y+h), (255, 0, 0), 2)
            blue_objects.append([(x + w)/2 , (y+h)/2])
            xb = x
            yb = y
            cv2.putText(frame,"BLUE",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))

            

    #Tracking the YELLOW Color
    
    contornosimg = yellow.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            yellow_objects.append([x+w/2 , y+h/2])
            cv2.putText(frame,"YELLLOW",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
            


    #Tracking the purple Color
    contornosimg = purple.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,255),2)
            purple_objects.append([x+w/2 , y+h/2])
            cv2.putText(frame,"purple",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    
          

    #Tracking the green Color
    
    contornosimg = green.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,255),2)
            green_objects.append([x+w/2 , y+h/2])
            cv2.putText(frame,"green",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    
            

    #Tracking the black Color
    
    contornosimg = black.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,255),2)
            black_objects.append([x+w/2 , y+h/2])
            cv2.putText(frame,"black",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    
             

    #Tracking the orange Color
    
    
    
    
   
    contornosimg = orange.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        # Eliminamos los contornos más pequeños
        if (cv2.contourArea(c) < 200):
            continue
        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        elif(cv2.contourArea(c) > 2000):
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,255),2)
            orange_objects.append([x+w/2 , y+h/2])
            cv2.putText(frame,"orange",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))

    
    
    
    if(xb==0):
        if(xr>(x1+30) or xr<(x1-30)):
            if(x1<xr):
                cv2.putText(frame,"Izquierda", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                horizontal = -1
            else: 
                cv2.putText(frame,"Derecha", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                horizontal = 1
            x1 = xr
        
        if(yr>(y1+30) or yr<(y1-30)):
            if(y1<yr):
                cv2.putText(frame,"Abajo", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                vertical = -1
            else:
                cv2.putText(frame,"Arriba", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                vertical = 1
            y1 = yr
            
            
            
    if(xb != 0):
        if(xb>(x2+30) or xb<(x2-30)):
            if(x1<xb):
                cv2.putText(frame,"Izquierda", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                horizontal = -1
            else: 
                cv2.putText(frame,"Derecha", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                horizontal = 1
            x2 = xb
        
        if(yb>(y2+30) or yb<(y2-30)):
            if(y2<yr):
                cv2.putText(frame,"Abajo", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                vertical = -1
            else:
                cv2.putText(frame,"Arriba", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                vertical = 1
            y2 = yb
        
    

    #########################################################################################

    if red_objects:
        finger_position_list[0].append(red_objects[0][0])
        finger_position_list[1].append(red_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    if blue_objects:
        finger_position_list[0].append(blue_objects[0][0])
        finger_position_list[1].append(blue_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    if yellow_objects:
        finger_position_list[0].append(yellow_objects[0][0])
        finger_position_list[1].append(yellow_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    if green_objects:
        finger_position_list[0].append(green_objects[0][0])
        finger_position_list[1].append(green_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    if purple_objects:
        finger_position_list[0].append(purple_objects[0][0])
        finger_position_list[1].append(purple_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    if orange_objects:
        finger_position_list[0].append(orange_objects[0][0])
        finger_position_list[1].append(orange_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    if black_objects:
        finger_position_list[0].append(black_objects[0][0])
        finger_position_list[1].append(black_objects[0][1])
    else:
        finger_position_list[0].append(0)
        finger_position_list[1].append(0)

    finger_position_list[0].append(horizontal*100)
    finger_position_list[1].append(vertical*100)


    #dev = 0
    if dev :
        print(string(finger_position_list[0]), string(finger_position_list[1]))
    else:
        if finger_position_list[0] != [] and finger_position_list[1] !=[]:
            try:
                final_sentence = comparate_with_database(finger_position_list[0], finger_position_list[1], database_name)
                if (final_sentence in 'jz'):
                    salidaFinal = final_sentence
                    counter = 11
                if(final_sentence == ""):
                    pass
                elif(final_sentence == "*"):
                    counter=0
                    if (mensaje != ""):
                        #send(mensaje)
                        print("Mensaje es ", mensaje)
                        msg_to_show += mensaje
                        mensaje = ""
                elif(final_sentence == salidaFinal):
                    print(final_sentence)
                    if(counter >= 10):
                        print (counter)
                        if(not isSend):
                            mensaje= mensaje + final_sentence
                            final_sentence = ""
                            isSend= True
                            counter+=1
                            print(mensaje)
                        else:
                            counter+=1
                    else:
                        print (counter)
                        counter+=1
                        print(final_sentence)
                else:
                    salidaFinal = final_sentence
                    counter=0
                    isSend=False


            except:
                print("Error")
                pass

            

    finger_position_list = [[], []]
    #cv2.putText(img2, 'hola', (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    
    cv2.imshow("Color Tracking", frame)
    cv2.moveWindow("Color Tracking",0, 0)

    img_sequence = np.zeros((600, 600, 3), np.uint8)

    #msg = "hola"
    #cv2.putText(img_sequence, msg, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.putText(img_sequence, msg_to_show, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    

    cv2.imshow('sequence', img_sequence)
    cv2.moveWindow("sequence", 800, 0)
    cv2.imshow("Color Tracking", frame)

    k = cv2.waitKey(10)
    if k == 27:
        break
    # N key
    if k == 110:
        database_name = 'numeros.csv'
        print("Database changed to numbers")

    # L key
    if k == 108:
        database_name = 'letras.csv'
        print("Database changed to letters")

    # P key
    if k == 112:
        database_name = 'provincias.csv'
        print("Database changed to provinces")

    # D key
    if k == 100:
        dev = not (dev)
        print('dev = ',dev)
