from jinja2 import Environment, PackageLoader
import inspect

def loadJS():
    pass
    
def loadCSS():
    pass

def renderPage():
    env = Environment(loader=PackageLoader('testpage.webpage', 'templates'))
    template = env.get_template('template.html')
    a = inspect.getfile(inspect.currentframe())
    return template.render(title='gyral - main',msg=a)
