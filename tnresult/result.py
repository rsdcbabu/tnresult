import cgi
import re
import time,datetime
import simplejson as json
import urllib

from google.appengine.api import users,urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):

        self.response.headers['Content-Type'] = 'text/html'
        txtweb_message = cgi.escape(self.request.get('txtweb-message'))
        self.response.out.write('<html><head><meta name="txtweb-appkey" content="app-id" /></head><body><b>Your Exam Results Will Be Declared Here Soon. Check This App Once It Is Announced.</b></body></html>')

application = webapp.WSGIApplication(
                                     [('/getresult', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

