import cv2
import face_recognition
import time
import numpy as np
from PIL import Image
import pickle as cPickle
import threading
import mysql.connector

table_name    = "userdata"
# insert_string = "INSERT into %s values (%s, %s, %s,%s,%s)" % (table_name)
update_string = "UPDATE %s SET name=?, status=? WHERE id=?" % (table_name)
select_true_string = "SELECT id,encoding,name,photo FROM %s WHERE status=1" % (table_name)
select_false_string = "SELECT id,encoding,name,photo FROM %s WHERE status=0" % (table_name)

host="localhost"
user="root"
password=""
database="face"
def get_userdata():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    cursor = mydb.cursor(dictionary=True)
    data=[]
    cursor.execute("select * from userdata;")
    rows=cursor.fetchall()
    if rows != None:
        for row in rows:
            data.append(row)
    mydb.commit()
    return data
def get_cameras():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    cursor = mydb.cursor(dictionary=True)
    data=[]
    cursor.execute("select * from cameras")
    rows=cursor.fetchall()
    if rows != None:
        for row in rows:
            data.append(row)
    mydb.commit()
    return data

def updateUserInDB(id,name):
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    
    mycursor = mydb.cursor()
    q="Update userdata set name='"+ name +"' , status=1 where id='"+id+"'"
    mycursor.execute(q)
    mydb.commit()

def insert_into_db(obj):
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT into userdata values (%s, %s, %s,%s,%s)",obj)
    mydb.commit()


def update_in_db(cursor, obj):
    cursor.execute(update_string,obj)

def knownUsers():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    cursor = mydb.cursor()
    data=[]
    cursor.execute(select_true_string)
    rows=cursor.fetchall()
    if rows != None:
        for row in rows:
            data.append(row)
    mydb.commit()
    return data

def unknownUsers():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    cursor = mydb.cursor()   
    data=[]
    cursor.execute(select_false_string)
    rows=cursor.fetchall()
    if rows != None:
        for row in rows:
            data.append(row)
    mydb.commit()
    return data

def checkKnownFace(encoding):
    try:
        rows=knownUsers()
        if(len(rows)>0):
            for row in rows:
                en=cPickle.loads(row[1])[0]
                if face_recognition.compare_faces([encoding],np.array(en),0.6)[0]:
                    return True,row[2]
        return False,'unknown'
    except Exception as e:
        print(e)
        return False,'unknown'

def checkAlreadyInDataset(encoding):
    try:
        rows=unknownUsers()
        if(len(rows)>0):
            for  row in rows:
                en=cPickle.loads(row[1])[0]
                if face_recognition.compare_faces([encoding],np.array(en),0.5)[0]:
                    return True,'Partially Known',row[0]
        return False,'unknown',None
    except Exception as e:
        print("error in already check")
        print(e)
        return False,'unknown',None
        
macURL='face_Recognition/data.csv'
winURL='data.csv'

import random
def fromFrame(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    loc = face_recognition.face_locations(rgb)
    encodings=face_recognition.face_encodings(rgb,model="hog")
    totalFaces=len(encodings)

    for i,face_location in enumerate(loc):
        topx, righty, bottomw, lefth = face_location
        personName="unknown"

        # if any face
        if(totalFaces>0):
        #   if face is know
            status,name=checkKnownFace(encodings[i])
            if(status):
                # get name of face from dataset
                personName=name
        #   face not known
            else:

                # if already added in dataset
                status,name,index=checkAlreadyInDataset(encodings[i])
                if(status):
                    # name partially known
                    personName=name
                # not present in dataset
                else:
                    # add to dataset
                    faceImage = frame[topx:bottomw+5, lefth:righty+5]
                    final = Image.fromarray(faceImage)
                    en=np.array(encodings[i])
                    # conn = sqlite3.connect('example.db')
                    row={'name':'unknown','encoding':cPickle.dumps([en]),'status':False,'id':str(int(time.time()))+str(random.randint(0,10000))}
                    picName="img%s.png" % (str(row['id']))
                    task=(row['id'],row['name'],row['encoding'],row['status'],picName)
                    insert_into_db(task) 
                    cv2.imwrite("static/images/"+picName,faceImage)                    


            p1,p2=(lefth,topx),(righty,bottomw)
            cv2.rectangle(frame,p1,p2,(0,255,0),3)
            cv2.putText(frame,personName,(lefth,topx),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    return totalFaces,frame


#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_recognized_frame(self):
        image = self.frame
        totalFaces,image=fromFrame(image)
        cv2.putText(image,"Total: "+str(totalFaces),(50,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
class LiveWebCam(object):
    def __init__(self,link):
        self.video = cv2.VideoCapture(link)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_recognized_frame(self):
        image = self.frame
        totalFaces,image=fromFrame(image)
        cv2.putText(image,"Total: "+str(totalFaces),(50,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

