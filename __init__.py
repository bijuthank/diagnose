from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Biju Thankachan'
LOGGER = getLogger(__name__)

class HelpMeSkill(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("").require("disease.details"))
    def handle_knock_knock_intent(self, message):# They said help me
        self.speak_dialog("disease")
# class Diagnose(MycroftSkill):

#     @intent_handler(IntentBuilder("").require("disease.details"))
#     def handle_diagnose_intent(self, message):
#         self.speak_dialog("disease")

def create_skill():
    return Diagnose()


