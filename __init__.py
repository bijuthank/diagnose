from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Lucas Vogel'
LOGGER = getLogger(__name__)


class Diagnose(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("").require("diagnose.invocation"))
    def handle_Diagnose_intent(self, message):
        if self.ask_yesno("disease") == 'yes':
            self.speak("otherinformation")
        
        #response = self.get_user_response("yes.response")
        #if response  == "yes":
            
        #self.speak_dialog("otherinformation")

def create_skill():
    return Diagnose()


