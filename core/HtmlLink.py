class HtmlLink:
    
    js_link_template = '<script type="text/javascript" src="%(name)s"></script>'
    css_link_template = '<link rel="stylesheet" href="%(name)s" type="text/css">'
    
    def __init__(self):
        self.jslinks = []
        self.csslinks = []
    
    def addJsLink(self, name):
        subst = {'name': name}
        self.jslinks.append(self.js_link_template % subst)
        return True
    
    def getJsLinks(self):
        return '\n'.join(self.jslinks)
    
    def addCssLink(self, name):
        subst = {'name': name}
        self.csslinks.append(self.css_link_template % subst)
        return True
    
    def getCssLinks(self):
        return '\n'.join(self.csslinks)
