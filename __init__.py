from mycroft import MycroftSkill, intent_file_handler


class Podcasts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('podcasts.intent')
    def handle_podcasts(self, message):
        self.speak_dialog('podcasts')


def create_skill():
    return Podcasts()

