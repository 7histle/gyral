from jinja2 import Environment, PackageLoader
import core.HtmlLink

def renderPage(links,cur_dir):
    env = Environment(loader=PackageLoader('testpage.webpage', 'templates'))
    template = env.get_template('template.html')
    links.addJsLink('http://code.jquery.com/jquery-latest.min.js') # jquery first
    links.addJsLink(cur_dir+'/testpage/templates/js/script.js')
    links.addCssLink(cur_dir+'/testpage/templates/css/style.css')
    return template.render(title='gyral - main',script=links.getJsLinks(),style=links.getCssLinks())
