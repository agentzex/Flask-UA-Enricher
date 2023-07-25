from flask import Flask, request
from flask_ua_enricher import SecChUa, resend_request_with_ch_ua


my_app = Flask(__name__)

sec_ch_ua = SecChUa()
sec_ch_ua.init_app(my_app)


@my_app.route('/helloChrome', methods=['GET'])
@resend_request_with_ch_ua
def hello():
    return f"{request.user_agent.string}"
