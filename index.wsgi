from webob import Request
import sys
import os
import inspect

# include current dir to the path
cur_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cur_folder not in sys.path:
    sys.path.insert(0, cur_folder)

def webob_wrap(func):
    def wrapped(environ, start_response):
        req = Request(environ)
        app = func(req)
        return app(environ, start_response)
    return wrapped

@webob_wrap
def main_index(req):
    return ShowPage()

from webob import Response
from testpage.webpage import renderPage

def ShowPage():
	ans = renderPage()
	return Response(ans)

application = main_index
