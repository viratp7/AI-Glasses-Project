import pyttsx3
import os


os.makedirs("audio", exist_ok=True)


engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


audio_phrases = {
    "Person in front": "person_in_front.wav",
    "Car in front": "car_in_front.wav",
    "Chair in front": "chair_in_front.wav",
    "Bicycle in front": "bicycle_in_front.wav",
    "Stop sign ahead": "stop_sign.wav",
    "Keyboard in front": "keyboard_in_front.wav",
    "Phone in front": "phone_in_front.wav",
    "Stop sign ahead": "stop_sign.wav",
    "Mouse in front": "mouse_in_front.wav",
}

for phrase, filename in audio_phrases.items():
    file_path = os.path.join("audio", filename)

    print(f"Generating: {phrase}")
    engine.save_to_file(phrase, file_path)

engine.runAndWait()

print("Done generating audio files.")