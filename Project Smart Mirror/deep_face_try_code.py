import cv2
from play_music import play_audio
from deepface import DeepFace
import time


RES = []
def detect_emotions(result_list):
    
    face_cascade = cv2.CascadeClassifier('/home/akshay/Desktop/practise/Project Smart Mirror/Haarcascade_face/haarcascade_frontface.xml')

    cap = cv2.VideoCapture(0)
    emotions_results = []
    start_time = time.time()
    while True:
        ret,frame = cap.read()
        result = DeepFace.analyze(img_path = frame , actions=['emotion'], enforce_detection=False )

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

        emotion = result["dominant_emotion"]
        emotions_results.append(emotion)
        RES.append(emotion)
            
        txt = emotion

        cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        cv2.imshow('frame',frame)

        # if time.time() - start_time >=5:
        #     break
            
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    text = emotions_results[-1]
    result_text = RES[-1]
    result_list.append(result_text)
    result_text = RES[-1]
    
    

