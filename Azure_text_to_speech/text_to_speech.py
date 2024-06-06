import os
import sys
import azure.cognitiveservices.speech as speechsdk

def synthesize_text_to_speech(text, output_file="output.wav"):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'

    # Create a speech synthesizer object
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Synthesize the speech
    result = speech_synthesizer.speak_text_async(text).get()

    # Check if the speech synthesis was successful
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized for text: {text}")

        # Save the synthesized audio to a file
        with open(output_file, "wb") as file:
            file.write(result.audio_data)

        print(f"Audio saved to: {output_file}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print(f"Error details: {cancellation_details.error_details}")
                print("Did you set the speech resource key and region values?")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the text to synthesize.")
        sys.exit(1)
    
    text_to_synthesize = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.wav"
    synthesize_text_to_speech(text_to_synthesize, output_file)
