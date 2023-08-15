import cv2
import numpy as np
from tensorflow.keras.models import load_model
import face_recognition

# Load pre-trained emotion recognition model
emotion_model = load_model('emotion_model.h5')

# Define emotion labels
emotion_labels = ['happy', 'sad', 'angry', 'disgusted', 'surprised', 'fearful', 'neutral']

def load_models():
    print("Models loaded successfully")

def initialize_webcam():
    video_capture = cv2.VideoCapture(1)
    return video_capture

def detect_faces_and_expressions(frame):
    # Detect faces
    face_locations = face_recognition.face_locations(frame)

    detections = []
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        face_image = cv2.resize(face_image, (64, 64))
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        face_image = np.expand_dims(face_image, 0)
        face_image = np.expand_dims(face_image, -1)

        # Predict emotion
        emotion_prediction = emotion_model.predict(face_image)
        emotion_label = emotion_labels[np.argmax(emotion_prediction)]
        detections.append(emotion_label)

    return detections

def display_emotion_counts(detections):
    emotion_counts = {label: 0 for label in emotion_labels}
    for detection in detections:
        emotion_counts[detection] += 1

    print(emotion_counts)

def run_emotion_detection():
    load_models()
    video_capture = initialize_webcam()

    while True:
        ret, frame = video_capture.read()

        frame = cv2.resize(frame, (700, 400))
        
        detections = detect_faces_and_expressions(frame)
        display_emotion_counts(detections)
        
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

run_emotion_detection()