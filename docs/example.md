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

