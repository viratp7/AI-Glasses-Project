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
