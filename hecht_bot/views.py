import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from slackclient import SlackClient          

from .api_keys import SLACK_VERIFICATION_TOKEN 
from .api_keys import SLACK_BOT_USER_TOKEN
from .utils import handle_helper_adding
from .utils import next_weekday

                                 
Client = SlackClient(SLACK_BOT_USER_TOKEN)                        


class Events(APIView):
    def post(self, request, *args, **kwargs):
        slack_message = request.data

        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message, status=status.HTTP_200_OK)

        if 'event' in slack_message:
            event_message = slack_message.get('event')
            channel = event_message.get('channel')
            if event_message.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)   

            user = event_message.get('user')                      
            text = event_message.get('text')   

            if 'montag' in text.lower():
                next_monday = next_weekday(datetime.date.today(), 0)
                next_monday_verbose = next_monday.strftime('%d. %b, %Y')
                if 'wochen' in text.lower():
                    week_amount = [int(s) for s in text.split() if s.isdigit()]
                    print('Wochen: ', week_amount)
                    if len(week_amount) != 1:
                        bot_text = 'Hi <@{}>, wenn du "Wochen" in deiner Nachricht erwähnst musst du genau eine ' \
                                   'Zahl in deiner Nachricht mitliefern, die Anzahl der Wochen' \
                                   ' die du vorausplanst.'.format(user)
                        Client.api_call(method='chat.postMessage',
                                        channel=channel,
                                        text=bot_text)
                        return Response(status=status.HTTP_200_OK)
                    print(next_monday_verbose)
                    handle_helper_adding(next_monday, user, week_amount[0])
                    bot_text = 'Hi <@{}>, du hast dich erfolgreich für die nächsten {} Montage eingetragen.'.format(
                        user,
                        week_amount[0])
                    Client.api_call(method='chat.postMessage',
                                    channel=channel,
                                    text=bot_text)
                    return Response(status=status.HTTP_200_OK)
                handle_helper_adding(next_monday, user)
                bot_text = 'Hi <@{}>, du hast dich erfolgreich für nächsten Montag eingetragen, den {}'.format(
                    user,
                    next_monday_verbose)
                Client.api_call(method='chat.postMessage',
                                channel=channel,
                                text=bot_text)
                return Response(status=status.HTTP_200_OK)

            if 'freitag' in text.lower():
                next_friday = next_weekday(datetime.date.today(), 4)
                next_friday_verbose = next_friday.strftime('%d. %b, %Y')
                if 'wochen' in text.lower():
                    week_amount = [int(s) for s in text.split() if s.isdigit()]
                    print('Wochen: ', week_amount)
                    if len(week_amount) != 1:
                        bot_text = 'Hi <@{}>, wenn du "Wochen" in deiner Nachricht erwähnst musst du genau eine ' \
                                   'Zahl in deiner Nachricht mitliefern, die Anzahl der Wochen' \
                                   ' die du vorausplanst.'.format(user)
                        Client.api_call(method='chat.postMessage',
                                        channel=channel,
                                        text=bot_text)
                        return Response(status=status.HTTP_200_OK)
                    handle_helper_adding(next_friday, user, week_amount[0])
                    bot_text = 'Hi <@{}>, du hast dich erfolgreich für die nächsten {} Freitage eingetragen.'.format(
                        user,
                        week_amount[0])
                    Client.api_call(method='chat.postMessage',
                                    channel=channel,
                                    text=bot_text)
                    return Response(status=status.HTTP_200_OK)
                handle_helper_adding(next_friday, user)
                bot_text = 'Hi <@{}>, du hast dich erfolgreich für nächsten Freitag eingetragen, den {}'.format(
                    user,
                    next_friday_verbose)
                Client.api_call(method='chat.postMessage',
                                channel=channel,
                                text=bot_text)
                return Response(status=status.HTTP_200_OK)

            if 'samstag' in text.lower():
                next_saturday = next_weekday(datetime.date.today(), 5)
                next_saturday_verbose = next_saturday.strftime('%d. %b, %Y')
                if 'wochen' in text.lower():
                    week_amount = [int(s) for s in text.split() if s.isdigit()]
                    print('Wochen: ', week_amount)
                    if len(week_amount) != 1:
                        bot_text = 'Hi <@{}>, wenn du "Wochen" in deiner Nachricht erwähnst musst du genau eine ' \
                                   'Zahl in deiner Nachricht mitliefern, die Anzahl der Wochen' \
                                   ' die du vorausplanst.'.format(user)
                        Client.api_call(method='chat.postMessage',
                                        channel=channel,
                                        text=bot_text)
                        return Response(status=status.HTTP_200_OK)
                    handle_helper_adding(next_saturday, user, week_amount[0])
                    bot_text = 'Hi <@{}>, du hast dich erfolgreich für die nächsten {} Samstage eingetragen.'.format(
                        user,
                        week_amount[0])
                    Client.api_call(method='chat.postMessage',
                                    channel=channel,
                                    text=bot_text)
                    return Response(status=status.HTTP_200_OK)
                handle_helper_adding(next_saturday, user)
                bot_text = 'Hi <@{}>, du hast dich erfolgreich für nächsten Samstag eingetragen, den {}'.format(
                    user,
                    next_saturday_verbose)
                Client.api_call(method='chat.postMessage',
                                channel=channel,
                                text=bot_text)
                return Response(status=status.HTTP_200_OK)

        # greet bot
        if 'event' in slack_message:                              
            event_message = slack_message.get('event')            
            
            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':     
                return Response(status=status.HTTP_200_OK)        
            
            # process user's message
            user = event_message.get('user')                      
            text = event_message.get('text')                      
            channel = event_message.get('channel')                
            bot_text = 'Hi <@{}> :wave:'.format(user)             
            if 'hi' in text.lower():                              
                Client.api_call(method='chat.postMessage',        
                                channel=channel,                  
                                text=bot_text)                    
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)
