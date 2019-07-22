# from apns3 import APNs, Frame, Payload
#
# print("正在认证")
# apns = APNs(use_sandbox=True, cert_file='public.pem', key_file='private.pem')
# print("认证完成")
# token_hex = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
# payload = Payload(alert="test push hello", sound="default", badge=1)
# print("正在发送")
# apns.gateway_server.send_notification(token_hex, payload)
# print("发送成功")





# from APNSWrapper.notifications import APNSNotificationWrapper, APNSNotification
#
# wrapper = APNSNotificationWrapper('ck.pem',True)
#
# deviceToken = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
# message = APNSNotification()
# message.token(deviceToken)
# message.badge(1)
#
#
# wrapper.append(message)
# wrapper.notify()
# from apns import APNs, Frame, Payload
# apns = APNs(use_sandbox=True, cert_file='public.pem', key_file='private.pem')
# token_hex = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
# payload = Payload(alert='test connect', sound='default', badge=1)
# apns.gateway_server.send_notification(token_hex, payload)
# print("发送完成")



"""
使用github上面的apns 实现发推送消息的代码
"""
import os
import random
from apns import APNs, Frame, Payload
BASERDIR = os.path.abspath(os.path.dirname(__file__))
apn_dev_cert_path = os.path.join(BASERDIR, 'dev-cert.pem')
apn_dev_key_path = os.path.join(BASERDIR, 'dev-key-noec.pem')
# deviceToken = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
apns = APNs(use_sandbox=True, cert_file=apn_dev_cert_path, key_file=apn_dev_key_path)
token_hex = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
payload = Payload(alert='hello just a test', sound='default', badge=2)
identifier = random.getrandbits(32)
apns.gateway_server.send_notification(token_hex, payload)
print("发送完成")
#



# from pushjack import APNSClient
#
# client = APNSClient(certificate=apn_dev_cert_path,
#                     default_error_timeout=100,
#                     default_expiration_offset=2592000,
#                     default_batch_size=100,
#                     default_retries=5)
#
# token = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'
# alert = 'Hello world.'

# Send to single device.
# NOTE: Keyword arguments are optional.
# res = client.send(token,
#                   alert,
#                   badge=2,)
# print(res)
# from apnsclient import *
# session = Session()
# con = session.get_connection("push_sandbox",cert_file=apn_dev_cert_path)
# message = Message('ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b', alert='hello',badge=1)
# srv = APNs(con)
# res = srv.send(message)
# for token,reason in res.failed.items():
#     code, errmsg = reason
#     print(token,errmsg)
# #


"""
使用http2连接一直连接不上apns服务器
"""
from hyper import HTTPConnection, tls
import json
token = 'ac16e5344c0de2a626e2d3789a18c054e380060fb3165779a173a1d4bd8f905b'

payload = {
    'aps': {
        'alert': '测试推送',
        'sound': 'default',
        'badge': 1,
    }
}
headers = {
    "apns-topic": 'com.csdigit.movesx',
}

conn = HTTPConnection('api.development.push.apple.com:443', ssl_context=tls.init_context(cert_path=apn_dev_cert_path))
conn.request('POST', '/3/device/%s' % token, body=json.dumps(payload), headers=headers)
resp = conn.get_response()
d = resp.status
print(d)


