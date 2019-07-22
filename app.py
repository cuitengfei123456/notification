import os
import random
import logging
from flask import Flask, request, jsonify
from apns import APNs, Frame, Payload, PayloadAlert

app = Flask(__name__)

BASERDIR = os.path.abspath(os.path.dirname(__file__))
handler = logging.FileHandler('notification.log', encoding='UTF-8')
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
)
handler.setFormatter(logging_format)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
apn_dev_cert_path = os.path.join(BASERDIR, 'dev-cert.pem')
apn_dev_key_path = os.path.join(BASERDIR, 'dev-key-noec.pem')
apns = APNs(use_sandbox=True, cert_file=apn_dev_cert_path, key_file=apn_dev_key_path, enhanced=True)


# 发送消息
def send_notification(token):
    payloads = Payload(alert='test connect', sound='default', badge=1)
    identifier = random.getrandbits(32)
    try:
        apns.gateway_server.send_notification(token, payloads, identifier=identifier)
        apns.gateway_server.register_response_listener(response_listener)
        return {'code': 200, 'state': 'success'}
    except Exception as e:
        app.logger.exception('push notification filed %s', e)


def response_listener(error_response):
    return ("client get error-response: " + str(error_response))


@app.route('/notification_api')
def hello_world():
    token_hex = request.args.get('token')
    # payload = request.args.get('payload')
    # token_hex = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
    resp = send_notification(token_hex)
    return resp


if __name__ == '__main__':
    app.run()
