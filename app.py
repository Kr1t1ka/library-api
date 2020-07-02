from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api_v1.main import create_app, db
from api_v1 import v1_api
from flask import url_for
import os
from flask_restx import Api


#TODO: закоммитить/раскоммитить перед пушем
#env_build = 'local'
env_build = os.getenv("BUILD") or 'dev'
app = create_app(env_build)
app.register_blueprint(v1_api, url_prefix='/api/v1')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    return "Hello world!"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'content-type,headers,authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == '__main__':
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')
    print(" * Running on {} build * ".format(env_build))
    if env_build == "prod":
        Api.specs_url = specs_url
    manager.run()