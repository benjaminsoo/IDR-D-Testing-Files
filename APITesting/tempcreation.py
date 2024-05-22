import requests

# Constants
BASE_URL = "https://voice-rest-api.idrnd.net"
API_KEY = "x-api-key"
HEADERS = {
    "x-api-key": API_KEY
}
TEMPLATE_ENDPOINT = "/voice_template_factory/create_voice_template_from_file"
AUDIO_FILE_PATH = "/Users/saiuser/Downloads/falsevoicetemplate1.wav" 

def create_voice_template(audio_file_path):
    files = {
        'wav_file': (audio_file_path, open(audio_file_path, 'rb'), 'audio/wav')
    }
    response = requests.post(
        BASE_URL + TEMPLATE_ENDPOINT,
        headers=HEADERS,
        files=files
    )
    return response.json()

def main():
    template_result = create_voice_template(AUDIO_FILE_PATH)
    print("Voice Template Result:", template_result)

if __name__ == "__main__":
    main()
