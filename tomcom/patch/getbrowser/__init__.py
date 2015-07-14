from OFS.SimpleItem import Item

def get_browser(self, name):

    return self.restrictedTraverse('@@'+name, None)

def getBrowser(self, name):

    return self.get_browser(name)


Item.get_browser = get_browser
Item.getBrowser = getBrowser
