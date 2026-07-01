from ultralytics import YOLO
import cv2
import pyttsx3
import time

model = YOLO("yolov8n.pt")

engine = pyttsx3.init()
engine.setProperty("volume", 1.0)

cap = cv2.VideoCapture(0)

last_spoken_time = 0
speak_cooldown = 3

while True:
    success, frame = cap.read()

    object_to_speak = None

    if not success:
        print("Could not read from webcam")
        break


    results = model(frame, verbose=False, stream=True)
    for result in results:
        boxes = result.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            
            if confidence > 0.6:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{class_name} {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                object_to_speak = class_name
                
     

                    
            
    current_time = time.time()
    if object_to_speak is not None:
        if current_time - last_spoken_time > speak_cooldown:
            engine.say(f" {object_to_speak} {object_to_speak} in front")
            engine.runAndWait()
            last_spoken_time = current_time


    cv2.imshow("AI Glasses YOLO Test", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()
