import datetime
import requests


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
    payload = {'token': 'xoxp-420436529250-487822130036-499705203062-ca29e339428a449bd84863ca5ae1211a',
               'user': '{}'.format(user_id)}
    json = requests.get('https://slack.com/api/users.info', params=payload).json()
    return json['user']['name']

