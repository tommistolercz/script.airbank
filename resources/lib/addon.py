from xbmcaddon import Addon
from xbmcplugin import getSetting, setContent, addDirectoryItems, addSortMethod, endOfDirectory, SORT_METHOD_NONE
from xbmcgui import ListItem
from sys import argv
from urlparse import parse_qs


class AirBankPlugin(object):

    # plugin initialization
    def __init__(self):
        self.addon = Addon()
        self.addonHandle = int(argv[1])
        self.urlBase = argv[0]  # 'plugin://script.airbank/'
        self.urlQuery = argv[2]  # '?foo=bar' (or empty)
        self.urlArgs = {}
        if self.urlQuery.startswith('?'):
            self.urlArgs = parse_qs(self.urlQuery.lstrip('?'))  # {'foo': ['bar']}
        self.userSettings = {
            'contentType': getSetting(self.addonHandle, 'contentType'),
        }
        setContent(self.addonHandle, self.userSettings['contentType'])
        self.dispatch()

    # plugin routing
    def dispatch(self):
        if (not self.urlArgs) or ('cwd' not in list(self.urlArgs)):
            self.dirRoot()
        else:
            pass

    # plugin directory: /
    def dirRoot(self):
        listItems = [
            ('{0}'.format(self.urlBase), ListItem('HELLO AIRBANK'), False),  # (item url, ListItem, isFolder) TODO: strings.po
        ]
        addDirectoryItems(self.addonHandle, listItems, len(listItems))
        addSortMethod(self.addonHandle, SORT_METHOD_NONE)
        endOfDirectory(self.addonHandle, updateListing=True, cacheToDisc=True)


# and action! ;-)
if __name__ == '__main__':
    AirBankPlugin()
