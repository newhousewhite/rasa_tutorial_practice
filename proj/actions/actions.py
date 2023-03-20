# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ActionReverted

import mysql.connector


hostname = "localhost"
username = "rasa-user"
password = "password123"
database = "shopping_db"

ALLOWED_PIZZA_SIZES = ["small", "medium", "large", "extra-large", "extra large", "s", "m", "l", "xl"]
ALLOWED_PIZZA_TYPES = ["mozzarella", "fungi", "veggie", "pepperoni", "hawaii"]


class ValidateSimplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_pizza_form"

    # name convention: validate_<slot_name>
    def validate_pizza_size(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'pizza_size' value."""
        if slot_value is None:
            return {"pizza_size": None}
        if slot_value.lower() not in ALLOWED_PIZZA_SIZES:
            dispatcher.utter_message(text=f"We only accept pizza sizes: s/m/l/xl.")
            return {"pizza_size": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"pizza_size": slot_value}

    # name convention: validate_<slot_name>
    def validate_pizza_type(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'pizza_type' value."""
        if slot_value is None:
            return {"pizza_type": None}

        if slot_value.lower() not in ALLOWED_PIZZA_TYPES:
            dispatcher.utter_message(text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}.")
            return {"pizza_type": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"pizza_type": slot_value}

# action_reset_problem
class ActionResetSimplePizzaForm(Action):
    def name(self) -> Text:
        return "reset_simple_pizza_form"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("pizza_size", None), SlotSet("pizza_type", None)]

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
        db = mysql.connector.connect(user=username, password=password, host=hostname, database=database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
        # category = 'laptop'
        category = tracker.get_slot('category')

        if category == 'phone':
            dispatcher.utter_message(text="phone news request is detected.")
            cursor.execute("SELECT blog_url FROM news WHERE category=%s LIMIT 3", ['mobile'])
        elif category == 'laptop':
            dispatcher.utter_message(text="laptop news request is detected.")
            cursor.execute("SELECT blog_url FROM news WHERE category=%s LIMIT 3", ['laptop'])
        # else:
        #     cursor.execute("SELECT blog_url FROM news")
        news = cursor.fetchall()
        if len(news) != 0:
            for x in news:
                dispatcher.utter_message(text=x[0])
        else:
            dispatcher.utter_message(text="Looks like there isn't any news available.")
        # dispatcher.utter_message(template='utter_select_next')
        return []
        #
        # dispatcher.utter_message(text="Here's the latest news for your category")
        # return []

# action_reset_problem
class ActionResetLatestNewsForm(Action):
    def name(self) -> Text:
        return "reset_latest_news_form"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("category", None)]

class YourResidence(Action):

    def name(self) -> Text:
        return "action_your_residence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # calling the DB
        # calling an API
        # do anything
        # all calculations are done

        dispatcher.utter_message(response="utter_residence")

        # it reverts to the previous dialog flow itself
        return [UserUtteranceReverted(), ActionReverted()]
