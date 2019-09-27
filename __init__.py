from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Biju Thankachan'
LOGGER = getLogger(__name__)


class Diagnose(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("").require("diagnose.invocation"))
    def handle_Diagnose_intent(self, message):
        decision = self.ask_yesno("disease")
        if decision == "yes":
            d2 = self.ask_yesno("COPDprognosis")
            if d2 == "yes":
                d3 = self.ask_yesno("therapy")
            elif d2 == "no":
                self.speak_dialog("anythingElse")
        elif desicion == "no":
            self.speak_dialog("anythingElse")
        
        
        

def create_skill():
    return Diagnose()


