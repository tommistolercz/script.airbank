from sys import argv
from urlparse import parse_qs
from xbmcaddon import Addon
from xbmcgui import ListItem
from xbmcplugin import setContent, addDirectoryItems, endOfDirectory, addSortMethod, SORT_METHOD_NONE

# debug
# addon.xml: <import addon="script.module.web-pdb"/>
# import web_pdb; web_pdb.set_trace()


class AirBankPlugin(object):

    # plugin initialization
    def __init__(self):
        self.addon = Addon()
        self.handle = int(argv[1])
        self.url = argv[0]
        self.base = 'plugin://script.airbank'
        self.path = self.url.replace(self.base, '')
        self.query = argv[2]
        self.args = {}
        if self.query.startswith('?'):
            self.args = parse_qs(self.query.lstrip('?'))
        self.userSettings = {
            'contentType': self.addon.getSetting('contentType'),
            'itemsPerPage': int(self.addon.getSetting('itemsPerPage')),
            'apiKey': self.addon.getSetting('apiKey'),
        }
        setContent(self.handle, self.userSettings['contentType'])
        self.dispatch()

    # plugin routing
    def dispatch(self):
        if self.path == '/':
            self.listRoot()
        elif self.path == '/branches':
            self.listBranches()

    # plugin directory: /
    def listRoot(self):
        isFolder = True
        listItems = [
            (self.base + '/branches', ListItem(self.addon.getLocalizedString(30004)), isFolder),
        ]
        addDirectoryItems(self.handle, listItems, len(listItems))
        addSortMethod(self.handle, SORT_METHOD_NONE)
        endOfDirectory(self.handle)

    # plugin directory: /branches
    def listBranches(self):
        pass


# and action! ;-)
if __name__ == '__main__':
    AirBankPlugin()
