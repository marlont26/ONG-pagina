# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/login'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False