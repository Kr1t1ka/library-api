import os

postgres_database_url = os.getenv("DBURL")
db_name = os.getenv("NAME").lower()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_database_url + db_name
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class LocalConfig(Config):
    db_name = 'library'
    SQLALCHEMY_DATABASE_URI = postgres_database_url + db_name
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_database_url + db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    local=LocalConfig
)

key = Config.SECRET_KEY
