# **************************************************************************************
# WARNING: This is a static file, useful as a starting point. You may want to change it.
# **************************************************************************************

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for an assistant that schedules reminders and
# reacts to external events.

# class MyCustomAction(Action):
#     def name(self) -> Text:
#         return "action_name"
#     async def run(
#         self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = tracker.events

        rejections_counter = 0

        for x in a:
            if x['event'] == 'user':
                if x['parse_data']['intent']['name'] == 'reject':
                    rejections_counter += 1

        if rejections_counter == 1:
            mx = 'utter_convincing_kelly'
        else :
            mx = 'utter_goodbye_kelly'

        dispatcher.utter_message(response = mx)

        return []