from mycroft import MycroftSkill, intent_file_handler


class InformationOfficer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('officer.information.intent')
    def handle_officer_information(self, message):
        self.speak_dialog('officer.information')


def create_skill():
    return InformationOfficer()

