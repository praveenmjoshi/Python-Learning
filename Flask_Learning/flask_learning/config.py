
#Contains app related configurations

class Config:
    SECRET_KEY = 'c4f0fb87dc671f00262836821a8af65d' #generated from command line secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'