from celery.decorators import task
from celery.utils.log import get_task_logger
import csv

logger = get_task_logger(__name__)


@task(name="handle_csv_upload")
def handle_sensor_upload(f):
    """
        Reads incoming csv containing sensor data.

        Bulk loads data into respective databases
    """
    data = []
    csv.DictReader(open(f))
    # for each record
        # if record (task) exists, add to same
        # else serialize Record
        # serialize data into SensorEntry model

        # add to data

    # bulk load data
