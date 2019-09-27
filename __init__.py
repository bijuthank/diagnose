from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Biju Thankachan'
LOGGER = getLogger(__name__)


class Diagnose(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("").require("disease.details"))
    def handle_disease_intent(self, message):
        self.speak_dialog("disease")

    @intent_handler(IntentBuilder("").require("copd.details"))
    def handle_disease_intent(self, message):
        self.speak_dialog("COPDprognosis")

    @intent_handler(IntentBuilder("").require("therapy.details"))
    def handle_disease_intent(self, message):
        self.speak_dialog("therapy")






        
        
        

def create_skill():
    return Diagnose()


