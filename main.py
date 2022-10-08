import cv2
import numpy as np
import os
import face_recognition
from datetime import datetime
import csv

path = 'fotowajah'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


#def markAttendance(name):
    #with open('Attendance.csv', 'r+') as f:
     #   myDataList = f.readlines()


       # nameList = []
        #for line in myDataList:
         #   entry = line.split(',')
          #  nameList.append(entry[0])
         #   if name not in nameList:
          #      now = datetime.now()
           #     dtString = now.strftime('%H:%M:%S')
            #    f.writelines(f'\n{name},{dtString}')

#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
def recognition():
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        frame, img = cap.read()
# img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
# print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
            else:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)                
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "TIDAK TAU", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)                
                #retake()
            #markAttendance(name)

        cv2.imshow('Webcam', img)
        k=cv2.waitKey(1)
        if k%256 == 27:
            print("esc kluar")
            cam.release()
            cam.destroyAllWindows
            break

def retake():
    #buat camera
    cam = cv2.VideoCapture(0)
    counter = 0
    wajahDir = 'fotowajah'
    while True:
        ret, frame = cam.read()

        cv2.imshow("test",frame)
        k=cv2.waitKey(1)
        if k%256 == 27:
            print("esc kluar")
            break
        elif k%256==32 :
            #buat screnshoot sama masukin ke folder
            name=input("Masukkan nama : ")
            print(name)
            NPM=input("Masukkan NPM : ")
            print(NPM)
            img_name = name + "_" + NPM + ".png"
            cv2.imwrite(wajahDir + '/' +img_name, frame)
        #buat input ke csv (gagal)
           # csv1 = open("coba.csv", 'w', newline='')
           # tulis = csv.writer(csv1)
        #tup1= {name, NPM}
        #tulis.writerow('\n'+tup1)
            break

    cam.release()
    cam.destroyAllWindows

recognition()

        


#buat ss 