############################################################################################################################

    def get_user_response(self, dialog):
        response = self.get_response(diagnose.invocation)
    -    return response

    @intent_handler(IntentBuilder("").require("diagnose.invocation"))
    def handle_knock_knock_intent(self, message):# They said help me
        #ask for body part
        user_response = self.get_user_response("disease")

        if user_response == "Yes" or  user_response =="yes":
            user_response = self.get_user_response (# write the dialog name where interested is stored)
        elif user_response == "No" or user_response == "no":
            self.speak_dialog ("OK, can I help you with anything else")
        elif user_response 
        








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