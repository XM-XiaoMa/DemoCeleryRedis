import os
import sys

from flask import Flask


def get_config_file():
    project_path = '.'
    c = os.environ.get('hahahahahahha')
    if not c:
        c = os.path.join(project_path, 'app_config_local.py')
    return c


app = Flask(__name__)
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
app.config.from_pyfile(get_config_file())


def get_celery_config(environment_name, default_name, default_config_path=None):
    c = os.environ.get(environment_name)
    if c:
        module_path, module_name = os.path.split(c)
        sys.path.append(module_path)
        return module_name.split('.')[0]
    else:
        if default_config_path:
            sys.path.append(os.path.join(os.getcwd(), default_config_path))
        return default_name


agent_pack_flask_worker = app.config['AGENT_PACK_FLASK_WORKER']
agent_pack_flask_worker.config_from_object(get_celery_config('hahahahahahha', 'agent_pack_flask_celery_config_local'))
