import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

def arbitrage_finder():
    print("Starting arbitrage finder")

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

scheduler = BlockingScheduler(jobstores=jobstores)

scheduler.add_job(arbitrage_finder, 'interval', minutes=1)
scheduler.start()