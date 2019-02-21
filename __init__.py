from mycroft import MycroftSkill, intent_file_handler


class TipicoTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.tipico.intent')
    def handle_test_tipico(self, message):
        self.speak_dialog('test.tipico')


def create_skill():
    return TipicoTest()

