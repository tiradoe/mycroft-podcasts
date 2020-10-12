from mycroft import MycroftSkill, intent_file_handler
import feedparser
from mygpoclient import public


class Podcasts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('podcasts.intent')
    def handle_podcasts(self, message):
        client = public.PublicClient()
        toplist = client.get_toplist()

        for index, entry in enumerate(toplist):
            self.speak_dialog(entry.title)


def create_skill():
    return Podcasts()

