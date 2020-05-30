import datetime
import json
import os
import requests
import sched
import time


scheduler = sched.scheduler(time.time, time.sleep)

calls_per_second = os.environ.get('CALLS_PER_SECOND')
endpoint = os.environ.get('ENDPOINT')

scheduler_interval = 1.0 / int(calls_per_second)


def call_api():
    scheduler.enter(scheduler_interval, 1, call_api)

    response = requests.get(endpoint)
    elapsed = response.elapsed.total_seconds()
    status_code = response.status_code
    success = False
    if status_code == 200:
        success = True

    log_object = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "success": success,
        "status_code": status_code,
        "ttlb": elapsed
    }

    print(json.dumps(log_object))




if __name__ == '__main__':
    scheduler.enter(scheduler_interval, 1, call_api)
    scheduler.run()
