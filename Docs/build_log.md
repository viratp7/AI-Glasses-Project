# Build Log

## DATE: 2026-06-30
### What I Did: Created a basic code that detects objects in real time and attempts to use a TTS moudle to say it out loud in a three second interval. For the obejct detecting I used a pretrained YOLO model, specifically Yolo V8 nano. Allowing for lower latency. Furtheremore, the object's name only gets spoken if the detection model has a confidence above 60 percent. An important feature am planning to have in my AI glasses that does not tell vissually impaired users in accurate detections.
### What Worked: The detection part worked well and the filtering aspect of it. When you run the code it is able to give an audio output of what it detects only at the begining.
### What didn't Work: The audio output did not work after the first time when starting the code
### What I learned: I learned about diffrent Yolo models and how they compare and work. Also I learn about text to speech modules like that pyttxs3 mouldle. Also from my failure I learned that am going to have an efficient audio system for my code to run well
### Next Steps: I need find an efficient method to TTS audio output, that could be changing the moudle or finding a new way to relay the information the model detects back to the user. Because based on my research, the audio system in my code is essentially too slow compared to everything else. Making it fall behind and skip. However, this is speculation and am going to need to do further testing. 

## DATE: 2026-07-02
### What I Did: The previos issue was the code only said the text to speech one time, but after swapping the text to speech for a simple print function, I releize the TTS is too slow. Going to need to figure out whether if am going to use a diffrent TTS method or find another solution.

## DATE: 2026-07-24
### What I Did: Going to test possible solution to the tts function being too slow for the loop. Currently I store pre generated objects into a seperate file so the code can eassily call upon them. This fixed the issue of the code not being able to repeat an object or TTS a new object that is detected. However, I am going to need to a priority filter now where it detects multiple objects but only says the important ones. Also if two objects have the same level of priority the code needs to be able to say both of them. 

## DATE: 2026-07-24

### What I Did
- Created a basic priority scoring system that assigns a priority score to detected objects.
- Decided to switch formating of build log

### What I Learned
- List functions
- How to use the length of the bounding boxes to my advantage via position (thought it was just a visual aid)


## DATE: 2026-07-24

### What I Did
- Added the first layer of depth/reasoning to the priority system, the program calculates the horizontal distance from the center and then changes the score based on this. 
- The code can store multiple objects in a list, and sorts it based on the most priority
- The code is now able to store multiple of the same objects in one list, so that two "persons" can co exits. Did this through creating a seperate 'id' for each object adding the sound and priority score after it has been calculated.
- Fixed some errors that previouly I did not know affected the priority system: detection.sort(key=lambda obj: [obj][1], reverse=True) Changed to detection.sort(key=lambda obj: obj[1], reverse=True)

### Why I changed it
- The priority system helps me start seperating my project from object detection to assistive device
### Results
- Can store multiple objects and adds more score to objects closer to center

### Next Steps
- Naturally a proximity feature added to the project, but need hardware for that, like a sensor, which is going to occur later on when I get to building my proeject. So I will add a tracking feature to avoid recalculating everything all the time.
## DATE: 2026-07-24

### What I Did
- Added a botsory.yaml tracking system to my code, it can track moving objects and take into consideration a moving camera. I beleive it will help with object collision alerts. 

### Results
- Can track objects and give them IDS, than print all the information (for testing and iteration)
- Does not interfer with the current basic priority sub sysstem
- The audio still works
- Can assign two things with the same id.
- Uses the Id not the class name to alert the user

### Next Steps
- Far later add a object collision prediction and detection alerts
