# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#             # calling the DB
#             # calling an API
#             # do anything
#             # all calculations are done
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
            # calling the DB
            # calling an API
            # do anything
            # all calculations are done

        dispatcher.utter_message(text="Here are your search results")

        return []

class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # calling the DB
        # calling an API
        # do anything
        # all calculations are done

        dispatcher.utter_message(text="Here's the latest news for your category")

        return []