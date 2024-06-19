import datetime
import pytz


def get_time_delta(entered_at, leaved_at):
    return leaved_at - entered_at


def get_duration(visit):
    if not visit.leaved_at:
        visit.leaved_at = datetime.datetime.now()
        utc = pytz.utc
        visit.leaved_at = utc.localize(visit.leaved_at)
    time_delta = get_time_delta(visit.entered_at, visit.leaved_at)
    return str(time_delta).split(".")[0]


def is_visit_long(visit, minutes):
    seconds = minutes * 60
    time_delta = get_time_delta(visit.entered_at, visit.leaved_at)
    return bool(time_delta.total_seconds() > seconds and visit.leaved_at)
