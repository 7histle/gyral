from webob import Request
import sys
import os
import inspect

# include current dir to the path
folder_path = os.path.split(inspect.getfile(inspect.currentframe()))[0]
cur_folder = os.path.realpath(os.path.abspath(folder_path))
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
    peek = req.path_info_peek()
    if not peek:
        return ShowPage()
    else:
        # find a file by url, if it is exist
        f = open(folder_path+req.path_info, "r")
        return Response(f.read())

from webob import Response
from testpage.webpage import renderPage

def ShowPage():
	ans = renderPage()
	return Response(ans)

application = main_index
