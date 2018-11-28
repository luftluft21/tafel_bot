from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient          

from .utils import handle_weekday_commands
from .api_keys import SLACK_CLIENT_ID
from .api_keys import SLACK_CLIENT_SECRET
from .api_keys import SLACK_VERIFICATION_TOKEN 
from .api_keys import SLACK_BOT_USER_TOKEN 

                                 
Client = SlackClient(SLACK_BOT_USER_TOKEN)                        


class Events(APIView):
    def post(self, request, *args, **kwargs):
        self.user_day_mapping = {}

        slack_message = request.data

        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if 'event' in slack_message:                              
            event_message = slack_message.get('event') 

            if event_message.get('subtype') == 'bot_message':     
                return Response(status=status.HTTP_200_OK)   

            user = event_message.get('user')                      
            text = event_message.get('text')   

            if 'montag' in text.lower():
                self.user_day_mapping = handle_weekday_commands(user, 0, self.user_day_mapping)
                print(self.user_day_mapping)
                return Response(status=status.HTTP_200_OK)

            if 'freitag' in text.lower():
                self.handle_weekday_commands(user, 4, self.user_day_mapping)
                print(self.user_day_mapping)
                return Response(status=status.HTTP_200_OK)

            if 'samstag' in text.lower():
                self.handle_weekday_commands(user, 5, self.user_day_mapping)
                print(self.user_day_mapping)
                return Response(status=status.HTTP_200_OK)

            # if check_for_content_in_message(message, 'hilfe') or check_for_content_in_message(message, 'Hilfe'):
            #     handle_weekday_commands(message, 0)


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