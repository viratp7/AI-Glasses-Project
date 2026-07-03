# Build Log

## DATE: 2026-06-30
### What I Did: Created a basic code that detects objects in real time and attempts to use a TTS moudle to say it out loud in a three second interval. For the obejct detecting I used a pretrained YOLO model, specifically Yolo V8 nano. Allowing for lower latency. Furtheremore, the object's name only gets spoken if the detection model has a confidence above 60 percent. An important feature am planning to have in my AI glasses that does not tell vissually impaired users in accurate detections.
### What Worked: The detection part worked well and the filtering aspect of it. When you run the code it is able to give an audio output of what it detects only at the begining.
### What didn't Work: The audio output did not work after the first time when starting the code
### What I learned: I learned about diffrent Yolo models and how they compare and work. Also I learn about text to speech modules like that pyttxs3 mouldle. Also from my failure I learned that am going to have an efficient audio system for my code to run well
### Next Steps: I need find an efficient method to TTS audio output, that could be changing the moudle or finding a new way to relay the information the model detects back to the user. Because based on my research, the audio system in my code is essentially too slow compared to everything else. Making it fall behind and skip. However, this is speculation and am going to need to do further testing. 

