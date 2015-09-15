import sys
import plugin
import logging


class Reverser(plugin.Plugin):

    def __init__(self):
        plugin.Plugin.__init__(self, "reverser")
        logging.info("Reverser.__init__")
        print("REVERER!!!!!!!!!!!")

    @staticmethod
    def _reverse_string(text):
        return text[::-1]

    def on_pubmsg(self, server, source, target, message):
        logging.info("Reverser.privmsg")
        if message.startswith("!reverse"):
            self.privmsg(server, target, Reverser._reverse_string(message[8:]))

    def started(self, settings):
        logging.info("Reverser.onconnected %s", settings)

    def on_welcome(self, server, source, target, text):
        logging.info("Reverser.on_welcome %s %s %s %s", server, source, target, text)
        self.join(server, u"#platinumshrimp")

if __name__ == "__main__":
    sys.exit(Reverser.run())
