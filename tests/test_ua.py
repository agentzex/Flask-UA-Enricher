
def test_android_ua(client):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Model": "SM-S901B",
        "Sec-Ch-Ua-Platform-Version": "13.0.0",
        "Sec-Ch-Ua-Platform": "Android",
        "Sec-Ch-Ua-Mobile": "?1"
    }
    response = client.get('/helloChrome', headers=headers)

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Mozilla/5.0 (Linux; Android 13.0.0; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
