import datetime
import requests

from .models import Helper
from .models import HelpingEntry


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def handle_weekday_commands(user, day_code, user_day_mapping):
    work_day = next_weekday(datetime.date.today(), day_code)
    if work_day in user_day_mapping:
        user_day_mapping[work_day].append(user)
    else:
        user_day_mapping[work_day] = [user]
    return user_day_mapping


def get_username(user_id):
    payload = {'token': '',
               'user': '{}'.format(user_id)}
    json = requests.get('https://slack.com/api/users.info', params=payload).json()
    return json['user']['name']


def try_getting_helping_entry(date):
    try:
        helping_entry = HelpingEntry.objects.get(date=date)
    except HelpingEntry.DoesNotExist:
        helping_entry = HelpingEntry.objects.create(date=date)
    return helping_entry


def handle_helper_adding(date, user, week_amount=None):
    try:
        helper = Helper.objects.get(name=get_username(user))
    except Helper.DoesNotExist:
        helper = Helper.objects.create(name=get_username(user))
    if week_amount:
        for x in range(0, week_amount):
            helping_entry = try_getting_helping_entry(date)
            helping_entry.helper.add(helper)
            print(helping_entry)
            helping_entry.save()
            date += datetime.timedelta(weeks=1)
    else:
        helping_entry = try_getting_helping_entry(date)
        if not helper.helping_entries.filter(date=date).exists():
            helping_entry.helper.add(helper)
            helping_entry.save()
