import requests

# Constants
BASE_URL = "https://voice-rest-api.idrnd.net"
API_KEY = "x-api-key"
HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}
MATCH_ENDPOINT = "/voice_template_matcher/match_voice_templates"

# Your first template (the one you just created)
voice_template1 = "PHZ0My4xMD4KMAoxClI4NVNETlcKRlYgBMAAAABZvCQ7TbYWveE/jL1m4K08hUYcvkRM+7pSZqy6EScFPSyoDr4zYgO9mN99PIk/ZjsaZ4I9Zfv1O3EroT2pQxu+tpkHve1ExDtWT/28186kvJqoSb1JnnO9a4qzPRjTUr3FpIa9kCsvvaycpTw7clg7YwPCvOkDGr4d4UY8r2ODvTAMMD3ZNZE9q1dTva3fprkY9c29EReYvZmxvz1X+YI96FC0PLGoH70V5LK9ZnIIvigHgj1AMW698kTivVTMbz2y58G8fiecvTpLDjzjR1G9m/vvvbUxJr5DrDW7YlOTPWNhS70K5vk9Gz+jvW0kWD3A1zq95csavEqlwr0zN8E95YYCPr3Ntj3zf5E9BkhQvZCXmzuBRb48rZkgvRBgJr42g608xeXOPK6sSb2E2Dk9lDXJPR0cAz20Tmk9Jr0uPSxSqL03m1I9/9mJPcNs8L3OaUe9P3sevhkyET0tOgI9U0AtvP7EgD07YG88Mv5lvVtVMzz0O9E8OgiBORTPpLtJsyM9/nl/vSrw6rylNiC9NH8bPgEF7T2AcrQ8epIQOjfgLb5UYBU+PcmSvXnIlTxDWlg8fqKdvalFHD6IP5K8u0ogvcmlEj57TcE8q5aQvOtT6j3YiYG7NTkHvk9ep70a/pg8IOumPPSjjr1UFy29oHTVvSbRqz3Ze5u9IpCHPSSHqj1JLqk8jV9svfDwLj10AA+9stGNPcSoMTzHvha+gQHNPCGfKr3t1x698qcYPbWajL3jru+8uz4bPeIMgLzJWKU9aqudvUvblLzxx9+902o7PiRxHL5m9Bm9KE+WvXG0mb3CQbG7xRrZPYNo+73g8+m81WtvvdJRCj1UihY9rsljO0LEsL175sQ6IRELPdi+db2OYxY8xZ92vaQ67L1Ehcs9+pWgPFEukL3pvb48gfcJvIjtWT075249Yr74vAiSAjzz8ug877ZKPMuvoD241+S7bVj5OkjVIr4xQqk8faWhPaIYMT13iCA9zY62PWwfUD2OK+K92i9evdXP6zxGViAEAAAAADEKPC92dDMuMTA+Cg=="

# Your second template (for matching)
voice_template2 = "PHZ0My4xMD4KMAoxClI4NVNETlcKRlYgBMAAAABxdVg96atiPQ+1r7zZ7bk7Xs+sPLRwGb0AIoW9mC+RPWUg4zxAuvy9OO2kPHXsML0OwoA9jFajvW9W4ryD9R6++zOYPJf6gDvsJPK97LZ9u7jOWD3O8TI9zL5wvc69CT2bdnU8Yi/EPR35Gr3f+fI8h3/TPfv+crwdv2g9qRLPvISrqz3wK3E6w+HzPWGHZL2IYX08RkCjPI2Lob1n92U7g6VPvk6vFD7ndoK76ZDcvL7xor3ZHqo8DGJnPKwWsLyNhaU9PXLuvPK8Vj2my409wApuvWEfgj0olfU94Z70vESYJLzR/I492NKSvFrszjvZA6c9NrqKvAjXpDsa77c9C0mSPXcoc70dyiy9/+6MvDA7bj1767u836LaPWM1oryw2pc9AmStvd+CSj0ohFg+dGTMvaM1UD36fxQ+yRhpPeXB4TxH2KG76ZiVvWgFkL3yobE9LbSdvVgZir0IqlA9O3kHPkQnR73xzSs9MjuOvENaTzx3dLq9M9JBvCaSv7zknrg9DqDMPbfWhj2qOSe9l315PUogTD30ZVa9mnwGPUTLtb3Bts89vk0aPAHoob3ldTg8FlACPaUTTj0G6RO90d1XvfAzwTz4sgs9zGK3Pdi9MD4zADC9W1bMvancBD6dhRM9/86zO6c3Bb4JgHE93d8oPRWhprxoaqE9A1KEvYdQq7ws+QI+F0+wPddshb0MCJw9PK9APf8pdD2f26q9HwdBPfLChjy3wlE9tv6mvePltLyQqQG+2yebPRAg3r0gyc89Q4/WvN+KSr0e3u69iSRuPW13AD2nFRA+ti9ePHYTjb1fEtE9ho4DPXPDjD1/vrY90lJTPWkRdLyOHwM+gUDCvVrlODs1H1g9n+jFvBOmoz2dklU9lEO4PfKsLb6v+qE9kJ14vefoEb3yuYi9i8qJPPQTiT03nnm6+HrqPOXqsD0WYg0+5RbYvaLJ67xZJ9+8aMWovZHtQ7pv+EQ9tOXEPbFqVb0K5to9Rb5fPbjL1T1lcII9PfP9PNPySb1GViAEAAAAADEKPC92dDMuMTA+Cg=="

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
    print("Match Result:", match_result)

if __name__ == "__main__":
    main()
