# coding=utf-8
import os
import sys

from celery import Celery

sys.path.insert(0, os.getcwd())

agent_pack_flask_celery_env_name = 'AGENT_PACK_FLASK_CELERY_CONFIG'

try:
    module_path, module_name = os.path.split(os.environ.get(agent_pack_flask_celery_env_name))
    sys.path.append(module_path)
except:
    module_name = 'agent_pack_flask_celery_config_local'

celery = Celery('agent_pack_flask_worker')
celery.config_from_object(module_name)


class StartPackageTask(celery.Task):
    """云打包的task"""
    name = 'agent_pack_flask_start_package_task'

    def run(self, *args, **kwargs):
        print('===================================agent_pack_flask_start_package_task=================================')
