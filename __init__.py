from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Lucas Vogel'
LOGGER = getLogger(__name__)

class Diagnose(MycroftSkill):
    @intent_handler(IntentBuilder("").require("diagnose.invocation"))
    def handle_DiagnoseMe_intent(self, message):
        #if self.ask_yesno("disease") == 'yes':
        user_response = self.get_user_response("yes.response")
            self.speak_dialog("otherinformation")

 
def create_skill():
    return Diagnose()


