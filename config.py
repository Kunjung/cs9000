import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
RECAPTCHA_PUBLIC_KEY = '6LfC6x4UAAAAAM_37yVtTCbWTvj2A-1RYO02l1Ay'
RECAPTCHA_PRIVATE_KEY = '6LfC6x4UAAAAACIDnsKT32rAJkIuU7DD6B7EFPN9'