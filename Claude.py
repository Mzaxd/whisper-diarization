import requests


url = "https://xqtd520qidong.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer sk-n7pXtdotZwzrySjTA94e86Ea40Af46A2B58677A794CbEb09",
    "content-type": "application/json"
}
data = {
    "messages": [
        {
            "role": "user",
            "content": "A brief introduction about yourself and say hello!",
        }
    ],
    "model": "claude-instant-1-100k",
    "max_tokens_to_sample": 300,
}

response = requests.post(url, headers=headers, json=data)
print(response.text)