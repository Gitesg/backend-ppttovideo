import requests
import os 
def generate_and_save_audio_files(Title, explanations):
    """
    Generate and save audio files based on the provided explanations.

    Args:
    - Title (list): List of titles.
    - explanations (list): List of explanations corresponding to the titles.
    """
    intro_Audio = {}
    api_key = os.environ.get('azure') # Replace with your API key
    region = 'centralindia'
    endpoint = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'

    def rep(text):
        headers = {
            'Ocp-Apim-Subscription-Key': api_key,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'audio-24khz-160kbitrate-mono-mp3',
            'User-Agent': 'faculty-voices'
        }

        ssml_template = f"""
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>
            <voice name='en-US-JessaNeural'>{text}</voice>
        </speak>
        """
        try:
            response = requests.post(endpoint, headers=headers, data=ssml_template)
            response.raise_for_status()  # Raise exception for bad response status
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def save_audio_file(file_name, content):
        if content:
            try:
                with open(file_name, 'wb') as audio:
                    audio.write(content)
                print(f"File saved: {file_name}")
            except IOError as e:
                print(f"Error saving file {file_name}: {e}")
        else:
            print("Empty content received. File not saved.")

    for i, title in enumerate(Title):
        title_lower = title.lower()
        audio_content = rep(explanations[i])
        file_name = f'audio/{i}.mp3'
        save_audio_file(file_name, audio_content)

# Example usage:
# generate_and_save_audio_files(Title, explanations)
