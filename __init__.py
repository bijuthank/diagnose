from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Biju Thankachan'
LOGGER = getLogger(__name__)


class Diagnose(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    
    @intent_handler("diagnose.invocation")
    def handle_diagnose_intent(self, message):
        self.speak_dialog("disease")

    @intent_handler("copd.details")
    def handle_copd(self, message):
        self.speak_dialog("COPDprognosis")

    @intent_handler("therapy.details")
    def handle_who_made_you_intent(self, message):
        self.speak_dialog("therapy")
        
        
        

def create_skill():
    return Diagnose()


