from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Lucas Vogel'
LOGGER = getLogger(__name__)

class HelpMeSkill(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(disease)
        return response

    @intent_handler(IntentBuilder("").require("diagnose.invocation"))
    def handle_knock_knock_intent(self, message):# They said help me
        #ask for body part
        bodypart = self.get_user_response("disease")
        # They said the body part
        specificypart = self.get_user_response("what.exactly")
        #they specify the body part
        painlevel = self.get_user_response("pain.level")
        summary = "Okay, so in your " + bodypart + ", more specifically " + specificypart + ", you experience level " + painlevel + " pain."
        self.speak(summary)
        shouldcallambulance =self.get_user_response("serious")
        if shouldcallambulance == "yes": # if the patient needs an ambulance
            self.speak_dialog("calling.ambulance")
        else: # if the patient does not want an ambulance
            self.speak_dialog("not.calling.ambulance")

def create_skill():
    return HelpMeSkill()


