from celery import Celery

from application import agent_pack_flask_worker

agent_pack_flask_worker.send_task('agent_pack_flask_start_package_task', kwargs={})
agent_pack_flask_worker.close()
