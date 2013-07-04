import cgi
def hello_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return "Hello, world"

application = hello_app
