# coding=utf-8
from kombu import Queue, Exchange

__author__ = 'junhai'

BROKER_URL = 'redis://0.0.0.0:6379/0'

CELERYD_CONCURRENCY = 1
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

CELERY_DEFAULT_QUEUE = 'agent_pack_flask_default'

CELERY_QUEUES = (
    Queue(name='agent_pack_flask_start_package_queue', exchange=Exchange('agent_pack_flask_tasks'), routing_key='agent_pack_flask_start_package_route'),
    Queue(name='agent_pack_flask_push_package_queue', exchange=Exchange('agent_pack_flask_tasks'), routing_key='agent_pack_flask_push_package_route'),
)

CELERY_ROUTES = {
    'agent_pack_flask_start_package_task': {'queue': 'agent_pack_flask_start_package_queue', 'routing_key': 'agent_pack_flask_start_package_route'},
    'agent_pack_flask_push_package_task': {'queue': 'agent_pack_flask_push_package_queue', 'routing_key': 'agent_pack_flask_push_package_route'},
}
