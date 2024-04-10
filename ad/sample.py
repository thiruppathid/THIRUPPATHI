import speech_recognition as sr
from googletrans import Translator, LANGUAGES
import googletrans
def translate():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Set the source and destination language codes
    src_lang = ''
    dest_lang = 'en'

    # Get the user's desired source language
    print('Available Languages:')
    for code, name in LANGUAGES.items():
        print(f"{code} : {name}")
    while src_lang not in LANGUAGES.keys():
        src_lang = input('Enter source language code: ')

    # Start the recognition process
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    # Recognize speech using Google's Speech Recognition API
    try:
        print("Transcribing...")
        detected_lang = r.recognize_google(audio, language=src_lang)
        print(f"You said: {detected_lang}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    # Translate the recognized text to the destination language
    translator = Translator()
    translation = translator.translate(detected_lang, dest=dest_lang)

    # Print the translation
    print(f"Translated to {LANGUAGES[dest_lang]}: {translation.text}")
