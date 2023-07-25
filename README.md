
## Why it's needed

Starting Chrome 110 (https://developer.chrome.com/blog/user-agent-reduction-android-model-and-version/), Chrome reduced User-Agent string content sent by default by browsers in every request.
The new UA string is will look like this:

Before: user-agent includes Android version and device model:

``` Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36 ```

After: reduced user-agent with fixed Android version and device model:

``` Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36 ```


This Flask wrapper tries to fix this by decorating a chosen Flask view, and if the fixed Android version and model are observed, it will trigger a refresh request from the browser but with the high entropy sec-ch-ua HTTP headers in the response, that can give us more information about the client (device model, OS version etc).

  (You can read more about those Sec-CH-UA headers here https://developer.mozilla.org/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues)

The response from the browser after the resent request will then have an enriched Flask request.user_agent including the correct device model and Android version, that can also be later parsed in any standard user-agent parsers libs or APIs


## Quickstart

```
from flask import Flask, request
from flask_ua_enricher import SecChUa, resend_request_with_ch_ua

app = Flask(__name__)

sec_ch_ua = SecChUa()
sec_ch_ua.init_app(app)


@app.route('/helloChrome', methods=['GET'])
@resend_request_with_ch_ua
def hello():
    return f"Hello with enriched UA: {request.user_agent.string}" 
```


## Note

If you're running this in a dev environment (i.e. your local PC), make sure to run your Flask server with HTTPS otherwise the enrichment won't work
