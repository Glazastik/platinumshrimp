import sys
import plugin

from twisted.python import log


class Reverser(plugin.Plugin):

    def __init__(self):
        plugin.Plugin.__init__(self, "Reverser")

    @staticmethod
    def _reverseString(text):
        return text[::-1]

    def privmsg(self, server, user, channel, message):
        if message.startswith("!reverse"):
            self.say(server, channel, Reverser._reverseString(message[8:]))

if __name__ == "__main__":
    sys.exit(Reverser.run())
