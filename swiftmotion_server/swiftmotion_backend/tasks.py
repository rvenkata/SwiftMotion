from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="import_csv")
def import_csv(email, message):
    pass
