import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xa8\xa7\xf6\x83o\xd1\xe3zkI}j\xc5\x96X\x97'

    MONGODB_SETTINGS={
        'db' : 'UTA_Enrollement'
    }
