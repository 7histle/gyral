from jinja2 import Environment, PackageLoader
import os

def renderPage():
    env = Environment(loader=PackageLoader('testpage.webpage', 'templates'))
    template = env.get_template('template.html')
    return template.render(title='test',msg='Hello world!')
