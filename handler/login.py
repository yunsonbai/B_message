import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
    	username = self.get_argument('username')
    	passwd = self.get_argument('pwd')
    	self.render('main.html')