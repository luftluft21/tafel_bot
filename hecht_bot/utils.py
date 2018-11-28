import datetime

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

# verification challenge
# def handle_verification():
#     if slack_message.get('type') == 'url_verification':
#         return Response(data=slack_message,
#                         status=status.HTTP_200_OK)