import os
import pickle
from rsstory.rss import *
from crontab import CronTab


def setup_cron(fpath, time_between):
    tab = CronTab()
    cmd = os.path.join(os.getcwd(), 'venv', 'bin', 'python') + ' ' + os.path.join(os.getcwd(), 'rsstory', 'periodic.py') + ' ' + fpath
    cron_job = tab.new(cmd)
    minutes_between = time_between.total_seconds() / 60.0
    cron_job.minute.every(minutes_between)
    cron_job.comment = 'Job for {} at interval (minutes) {}'.format(fpath, minutes_between)
    tab.write()

    #TODO: remove the job once no longer needed

def update_feed(fpath):
    rss_items = pickle.load(open(fpath, "rb"))
    write_rss(rss_items)

if __name__ == "__main__":
    update_feed(sys.argv[1])
