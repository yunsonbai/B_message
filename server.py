import tornado.httpserver
import os.path
import tornado.options
import tornado.ioloop
import tornado.web
import handler 
from handler.index import IndexHandler
from handler.login import LoginHandler

from tornado.options import define,options
define('port',default=8000,help="run the the given port",type=int)

handlers=[(r'/',IndexHandler),
	(r'/login',LoginHandler)
	]
templates=os.path.join(os.path.dirname(__file__), "templates")
class Application(tornado.web.Application):
	def test(self):
		pass	
if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = Application(handlers=handlers,template_path=templates)
	http_server=tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()