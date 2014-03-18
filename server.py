#-*- coding: UTF-8 -*-
import os 
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from WordExtractor import *

from tornado.options import define, options
define("port", default=9876, help="run on the given port", type=int)


class EW(object):
    count = 0
    ew = WordExtracter('my_small.trie')
    ew.initStopWords('stop_words')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("new_cutter.html")


class ExtractHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/text')

    def get(self):
        greeting = self.get_argument('content', u'Vine, Twitter’s New Video Tool')
        entities = EW.ew.get_wiki_entities(greeting.lower())
        entities = sorted(entities.iteritems(),key=itemgetter(1),reverse=True)
        self.finish('\n'+str(entities))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/",IndexHandler),(r"/extract", ExtractHandler)],
        template_path=os.path.join(os.path.dirname(__file__),"templates"),
        static_path = os.path.join(os.path.dirname(__file__),"static"),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
