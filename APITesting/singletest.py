import requests

# Constants
BASE_URL = "https://voice-rest-api.idrnd.net"
API_KEY = "gJ2Ii8jqGw71gFL3stE6C9C7eXQ3KDH87hJBfd3e"
HEADERS = {
    "x-api-key": API_KEY
}
TEMPLATE_ENDPOINT = "/voice_template_factory/create_voice_template_from_file"
MATCH_ENDPOINT = "/voice_template_matcher/match_voice_templates"
AUDIO_FILE_PATH = "/Users/saiuser/Downloads/falsetemplate10.wav" 

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


# First Template
voice_template1 = "PHZ0My4xMD4KMAoxClI4NVNETlcKRlYgBMAAAABZvCQ7TbYWveE/jL1m4K08hUYcvkRM+7pSZqy6EScFPSyoDr4zYgO9mN99PIk/ZjsaZ4I9Zfv1O3EroT2pQxu+tpkHve1ExDtWT/28186kvJqoSb1JnnO9a4qzPRjTUr3FpIa9kCsvvaycpTw7clg7YwPCvOkDGr4d4UY8r2ODvTAMMD3ZNZE9q1dTva3fprkY9c29EReYvZmxvz1X+YI96FC0PLGoH70V5LK9ZnIIvigHgj1AMW698kTivVTMbz2y58G8fiecvTpLDjzjR1G9m/vvvbUxJr5DrDW7YlOTPWNhS70K5vk9Gz+jvW0kWD3A1zq95csavEqlwr0zN8E95YYCPr3Ntj3zf5E9BkhQvZCXmzuBRb48rZkgvRBgJr42g608xeXOPK6sSb2E2Dk9lDXJPR0cAz20Tmk9Jr0uPSxSqL03m1I9/9mJPcNs8L3OaUe9P3sevhkyET0tOgI9U0AtvP7EgD07YG88Mv5lvVtVMzz0O9E8OgiBORTPpLtJsyM9/nl/vSrw6rylNiC9NH8bPgEF7T2AcrQ8epIQOjfgLb5UYBU+PcmSvXnIlTxDWlg8fqKdvalFHD6IP5K8u0ogvcmlEj57TcE8q5aQvOtT6j3YiYG7NTkHvk9ep70a/pg8IOumPPSjjr1UFy29oHTVvSbRqz3Ze5u9IpCHPSSHqj1JLqk8jV9svfDwLj10AA+9stGNPcSoMTzHvha+gQHNPCGfKr3t1x698qcYPbWajL3jru+8uz4bPeIMgLzJWKU9aqudvUvblLzxx9+902o7PiRxHL5m9Bm9KE+WvXG0mb3CQbG7xRrZPYNo+73g8+m81WtvvdJRCj1UihY9rsljO0LEsL175sQ6IRELPdi+db2OYxY8xZ92vaQ67L1Ehcs9+pWgPFEukL3pvb48gfcJvIjtWT075249Yr74vAiSAjzz8ug877ZKPMuvoD241+S7bVj5OkjVIr4xQqk8faWhPaIYMT13iCA9zY62PWwfUD2OK+K92i9evdXP6zxGViAEAAAAADEKPC92dDMuMTA+Cg=="

# Second Template
voice_template2 = create_voice_template(AUDIO_FILE_PATH)

def match_voice_templates(template1, template2):
    data = {
        "template1": template1,
        "template2": template2
    }
    response = requests.post(
        BASE_URL + MATCH_ENDPOINT,
        headers=HEADERS,
        json=data
    )
    return response.json()

def main():
    match_result = match_voice_templates(voice_template1, voice_template2)
    print(match_result)

if __name__ == "__main__":
    main()
