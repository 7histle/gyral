from jinja2 import Environment, PackageLoader
from core.db.database import DataBase
from core.syspath import syspath

def renderPage(links):
    # just an example
    db = DataBase()
    if db.initBase():
        if db.insertSample('Hello World!'):
            res = db.getSample();
    a = ''
    for x in res:
        a += x[0]+'<br/>'
    env = Environment(loader=PackageLoader('testpage.webpage', 'templates'))
    template = env.get_template('template.html')
    links.addJsLink(syspath.BASE_DIR+'/testpage/templates/js/script.js')
    links.addCssLink(syspath.BASE_DIR+'/testpage/templates/css/style.css')
    return template.render(title='gyral - main',maintext=a,script=links.getJsLinks(),style=links.getCssLinks())
