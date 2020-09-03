#
# -*- coding:utf-8 -*-

import pyotp
import qrcode

"""
pyotp.TOTP -> 生成和校验一次性密码
qrcode  生成二维码图片
"""


# 基于 base32 密钥 生成一次性密码
# secret = pyotp.random_base32()
secret = "7BCLZDMS7R32NLHA"
totp = pyotp.TOTP(secret)

# 生成验证url
provisioning_uri = totp.provisioning_uri(name="admin",issuer_name="mzc_test")

# 获取当前6位密码
# print(totp.now())

# 验证6位一次性密码
# print totp.verify("186558")

# 生成二维码图片
img = qrcode.make(provisioning_uri)

with open("test_qr.png",'wb') as f:
    img.save(f)