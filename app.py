import os, sys
from twisted.python import log
from twisted.internet import reactor

import cyclone.web

class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]

        settings = dict(
            xheaders=False,
            static_path="./static",
            templates_path="./templates",
        )

        cyclone.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    log.startLogging(sys.stdout)
    port = int(os.getenv('OPENSHIFT_PYTHON_PORT', 8888))
    host = os.getenv('OPENSHIFT_PYTHON_IP', "0.0.0.0")
    reactor.listenTCP(port, Application(), interface=host)
    reactor.run()