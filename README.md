Azure text to speech:
setx SPEECH_KEY your-key
setx SPEECH_REGION your-region

Azure Open Ai
setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE"

text to speech usage:
python ./text_to_speech/text_to_speech.py "This is a test sentence for text to speech." test_output.wav

open Ai exaple usage:
python ./text_to_speech/text_to_speech.py "This is a test sentence for text to speech." test_output.wav