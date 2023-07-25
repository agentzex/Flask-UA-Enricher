from flask import make_response, request
from functools import wraps



class SecChUa:
    def __init__(self, app=None):
        if app:
            self.app = app
            self.init_app(app)


    def init_app(self, app):
        pass



html_refresh_page = """
<head>
<meta http-equiv="refresh" content="1">
</head>
"""

chrome_static_ua = "Android 10; K"


def _make_refresh_response_with_ch_ua():
    response = make_response(html_refresh_page)
    response.headers["Accept-CH"] = "Sec-CH-UA-Platform-Version, Sec-CH-UA-Model"  # more headers can be added here. See full list below
    return response


def resend_request_with_ch_ua(func):
    # in newer chrome version user-agent doesn't include device info anymore. This will request the browser to resend the request with sec-ch-ua values

    high_entropy_sec_ch_ua_headers = {
        "Sec-CH-UA-Arch": "",
        "Sec-CH-UA-Bitness": "",
        "Sec-CH-UA-Model": "",
        "Sec-CH-UA-Platform-Version": "",
        "Sec-CH-UA-Full-Version-List": "",
    }


    @wraps(func)
    def wrapper(*args, **kwargs):
        if chrome_static_ua not in request.user_agent.string:  # not reduced UA, we can use the normal request.user_agent
            return func(*args, **kwargs)

        # if new reduced UA, but we got any of the high entropy UA in the request headers from the browser
        if chrome_static_ua in request.user_agent.string and any(header in request.headers for header in high_entropy_sec_ch_ua_headers):
            for header in high_entropy_sec_ch_ua_headers:
                try:
                    high_entropy_sec_ch_ua_headers[header] = request.headers[header].replace('"', '')  # these headers have double quote
                except KeyError as e:
                    pass

            # replace the model and platform version attributes in user_agent
            request.user_agent.string = request.user_agent.string.replace(chrome_static_ua,
                                                                          f"Android {high_entropy_sec_ch_ua_headers['Sec-CH-UA-Platform-Version']}; {high_entropy_sec_ch_ua_headers['Sec-CH-UA-Model']}")
            return func(*args, **kwargs)

        return _make_refresh_response_with_ch_ua() # ask the browser to resend the request with high entropy ch-ua headers

    return wrapper










