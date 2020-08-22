from mycroft import MycroftSkill, intent_file_handler


class OpaEnergy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('energy.opa.intent')
    def handle_energy_opa(self, message):
        self.speak_dialog('energy.opa')


def create_skill():
    return OpaEnergy()

