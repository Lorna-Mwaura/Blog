import os

class Config:

    SECRET_KEY = ('123Qwe')
    SQLALCHEMY_DATABASE_URI = 'postgres://xmhxzefqgtqvvn:ff969f7dc966d4693085fd03bbaf174c009467728d5b6c91997ed649bd432cd1@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d20rk3iuqte2gj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}