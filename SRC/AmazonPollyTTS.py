import boto3
from pydub import AudioSegment
from pydub.playback import play

def polly_speak_text(text, filename="AudioOutput.mp3", voice="Joanna"):
    # Initialize the Polly client
    polly = boto3.client("polly")

    # Request speech synthesis with plain text
    response = polly.synthesize_speech(
        Text=text,
        TextType="text",  # <-- Use plain text here
        OutputFormat="mp3",
        VoiceId=voice
    )

    # Save the resulting audio to a file
    with open(filename, "wb") as file:
        file.write(response["AudioStream"].read())

    print(f"Saved audio to {filename}")

    # Load and play the audio
    # audio = AudioSegment.from_mp3(filename)
    # play(audio)