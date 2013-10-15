class HtmlLink:
    
    js_link_template = '<script type="text/javascript" src="%(name)s"></script>'
    css_link_template = '<link rel="stylesheet" href="%(name)s" type="text/css">'
    
    def __init__(self):
        self.jslinks = set()
        self.csslinks = set()
    
    def addJsLink(self, name):
        subst = {'name': name}
        self.jslinks.add(self.js_link_template % subst)
        return True
    
    def getJsLinks(self):
        return '\n'.join(self.jslinks)
    
    def addCssLink(self, name):
        subst = {'name': name}
        self.csslinks.add(self.css_link_template % subst)
        return True
    
    def getCssLinks(self):
        return '\n'.join(self.csslinks)
