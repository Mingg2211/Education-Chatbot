# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionResponseMajorInfo(Action):

    def name(self) -> Text:
        return "action_response_major_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Thông tin về ngành {major_name} info")
        return []


class ActionResponseMajorTypeEdu(Action):

    def name(self) -> Text:
        return "action_response_major_type_edu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Ngành {major_name} đào tạo những hệ ...")
        return []


class ActionResponseMajorPoint(Action):

    def name(self) -> Text:
        return "action_response_major_point"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Hiện tại chưa có điểm sàn của ngành {major_name}")
        return []


class ActionResponseMajorCareer(Action):

    def name(self) -> Text:
        return "action_response_major_career"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Cơ hội làm việc của ngành {major_name} ...")
        return []


class ActionResponseMajorTuition(Action):

    def name(self) -> Text:
        return "action_response_major_tuition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Học phí của ngành {major_name} ...")
        return []


class ActionResponseSubjectGroup(Action):

    def name(self) -> Text:
        return "action_response_major_subject_group"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Ngành {major_name} tuyển sinh các khối ...")
        return []


class ActionResponseMajorCriteria(Action):

    def name(self) -> Text:
        return "action_response_major_criteria"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        major_name = tracker.get_slot("major_name")
        if not major_name:
            dispatcher.utter_message(text="Tôi không hiểu")
        else:
            dispatcher.utter_message(
                text=f"Năm 2022 ngành {major_name} dự kiến tuyển sinh khoảng ... sinh viên")
        return []
