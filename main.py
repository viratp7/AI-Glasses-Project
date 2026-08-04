from ultralytics import YOLO
import cv2
import time
import pygame

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
pygame.mixer.init()
last_spoken_time = 0
speak_cooldown = 3
last_spoken_object = None

sounds = {
    "person": {
        "sound": pygame.mixer.Sound("audio/person_in_front.wav"),
        "priority": 2,
        "position_factor": 1.0,
        
    },
    "keyboard": {
        "sound": pygame.mixer.Sound("audio/keyboard_in_front.wav"),
        "priority": 1,
        "position_factor": 1.2,
        
    },
    "cell phone": {
        "sound": pygame.mixer.Sound("audio/phone_in_front.wav"),
        "priority": 1,
        "position_factor": 1.3,
        
    },
    "stop sign": {
        "sound": pygame.mixer.Sound("audio/stop_sign.wav"),
        "priority": 3,
        "position_factor": 1,
        
    },
    "mouse": {
        "sound": pygame.mixer.Sound("audio/mouse_in_front.wav"),
        "priority": 2,
        "position_factor": 1.4,
           
   }
}



while True:
    success, frame = cap.read()

    object_to_speak = None
    detection = []

    # Check if the frame was successfully read from the webcam
    if not success:
        print("Could not read from webcam")
        break


    results = model.track(frame, verbose=False, stream=True, tracker="botsort.yaml", persist=True)
    for result in results:

        #Check if something is detected in the frame
        if result.boxes is None:
            continue
        


        if result.boxes is not None and result.boxes.is_track:
            boxes = result.boxes.xyxy.cpu().tolist()
            track_ids = result.boxes.id.int().cpu().tolist()
            class_ids = result.boxes.cls.int().cpu().tolist()
            confidences = result.boxes.conf.cpu().tolist()
            
            for box, track_id, class_id, confidence in zip(boxes, track_ids, class_ids, confidences):

                x1, y1, x2, y2 = box
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                
                class_name = model.names[class_id]

                object_center_x = (x1 + x2) / 2
                object_center_y = (y1 + y2) / 2

                height, width = frame.shape[:2]
                frame_center_x = width / 2
                frame_center_y = height / 2


                if confidence > 0.6:
                    # print(box, track_id, class_id, confidence)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    label = f"{class_name} {confidence:.2f}"
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    if class_name in sounds:
                        distance_from_center = abs(object_center_x - frame_center_x)
                        normalized_distance = distance_from_center / (width / 2)
                        position_weight = 1 - normalized_distance
                        final_priority = sounds[class_name]["priority"] +(
                            position_weight * sounds[class_name]["position_factor"])
                        
                        detection.append((track_id, class_name, final_priority))
                
    if detection:
        print(detection)
        detection.sort(key=lambda obj: obj[2], reverse=True)
        object_to_speak = detection[0][0]
        name_to_speak = detection[0][1]
        priority_to_speak = detection[0][2]
     

                    
            
    current_time = time.time()
    if object_to_speak is not None:
        object_changed = object_to_speak != last_spoken_object
        if current_time - last_spoken_time > speak_cooldown and object_changed:
            sound = sounds[name_to_speak]["sound"]
            if sound is not None:
                sound.play()
                print(f"Speaking: {name_to_speak}, Priority: {priority_to_speak:.2f}, track_id: {object_to_speak}")
                # print(f"Priority: {priority_to_speak:.2f}")
                last_spoken_time = current_time
                last_spoken_object = object_to_speak



    cv2.imshow("AI Glasses YOLO Test", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()
