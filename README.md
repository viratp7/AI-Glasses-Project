# AI-Glasses-Project
Initial stage of a real-time object detection program that has TTS. Eventually it is going to be used for a low cost assistive medical device for the visually impaired, that uses AI models to read warnings/signs, warns them, alerts them for hazards, etc. 

The current/early versions of the software are prototyping and the skeleton of the project. It uses a pretrained YOLO object detection model to detect objects through my webcam. Right now it has a early TTS feature, but it does not work proper, intdent and still needs to be ironed out.

# Current Status
Currently the project is in it's early software stage, not even hardware
The current code can:
- Detect objects using YOLO
- Filter out the objects the model is not too confident in
- Say the object in front but does not say it again or any diffrent object
- Have a time filter for the TTS feature

# Project Goal
## Current
Since my project is in it's early stages I have short term goals and long term goals.
Short term Goals:
- Make TTS engine say diffrent objects and 
- Say detected objects more than once if their still detected pass the time limit
Based on my reasearch, the reason the TTS engine does not say the object more than once, it's because it's to slow since it uses my enternal OS to generate the audio

## LongTerm
I have many long term goals for the software that are based on the needs and wants of Vissually impaired individuals
Long Term Goals:
- Specfic Obstacal detection
- Custom trained YOLO model
- Able to detect text in real life and read it out loud
- Have a priority engine that only says the most important thing in frame so the user does not get notification fautigue or distracted from what is important
- Low Latency
- Efficient
- If detected, identify and say out loud the symbols of WHIMIS
- Road warnings

# Importance
There are alot of good AI vission tools for the vissually impaired like the envision glasses. Envision Glasses are smart glasses that give vissually impaired individuals to read things like documents and signs, have the world described to them, find objects etc. The envision glasses are amazing because of their compact size, efficincy and accuracy. However, they require an individual to activly call on their use and they're relativly exspensive. Meta Rayband Glasses are also a tool that can be used by the vissually impaired to read things, describe things etc. But like the envsion glasses they require an individual to activly call on their use.

The most important thing these two device do not do is automatic object detection played out loud. For example a vissually impaired person is walking in a mall with a wet floor ahead. With the Envsion and Meta glasses they would have to manuely call upon their assitance to notify them on what is going on. Which is bad because for a vissually impaired person it would be difficult for them to be notified by visual based cues and these Glasses are likely to describe uncessory things if the user ask them to "describe what is infront of me". 

With glasses am going to eliminate the need for a user to know when to use AI. The AI will filter out everything and notfiy the user automatically of important things that they should know like a wet floor sign.


# How to Run

Install the required libraries:
pip install -r requirements.txt

Run the main program:
python main.py

Note: The project currently requires a working webcam and is not complete at all


