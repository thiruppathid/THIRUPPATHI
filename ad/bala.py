import openai
import pyttsx3
from googletrans import Translator, LANGUAGES
import googletrans
import speech_recognition as sr
import pyaudio
# Initialize OpenAI API
openai.api_key = "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"
# Initialize the text to speech engine
engine = pyttsx3.init()
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
    print(translation.text)
    return translation.text


def transcribe_audio_to_test(filename):
    recogizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recogizer.record(source)

    try:
        return recogizer.recognize_google(audio)
    except:
        print("skipping unkown error")


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():

    while True:
        # Wait for user say "genius"
        print("Say 'Genius' to start recording your question")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if "genius" in transcription.lower():
                    # record audio
                    request=translate()
                    # transcript audio to test
                    text = request
                    if text:
                        print(f"you said : {text}")

                        # Generate the response
                        response = generate_response(text)
                        print(f"AI say: {response}")


                        # read resopnse using GPT3
                        speak_text(response)
            except Exception as e:

                print("An error ocurred : {}".format(e))


if "__main__" == __name__:
    main()