import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'c999f61d1e154e16fa1f0336af0d15e12cc810f5797cb6dd6997571950802f94')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}