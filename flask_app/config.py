SOME_CONFIG="configured in config.py"

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SOME_CONFIG = "configured in Config class in config.py"


class ProductionConfig(Config):
    DATABASE_URI = 'mysql:///user@localhost/foo'
    SOME_CONFIG = "configured in ProductionConfig class in config.py"


class DevelopmentConfig(Config):
    DEBUG = True
    SOME_CONFIG = "configured in DevelopmentConfig class in config.py"