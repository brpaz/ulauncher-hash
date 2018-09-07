import logging
import hashlib
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)

class HashExtension(Extension):
    def __init__(self):
        logger.info('init hash Extension')
        super(HashExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        argument = (event.get_argument() or '').encode('utf-8')
        keyword = event.get_keyword()

        # Find the keyword id using the keyword (since the keyword can be changed by users)
        for kwId, kw in extension.preferences.iteritems():
            if kw == keyword:
                keywordId = kwId[:-3] # Remove the "_kw" suffix

        # Show the algorithm specified as keyword, or all if the keyword was "hash"
        algos = hashlib.algorithms if keywordId == 'hash' else [keywordId]

        for algo in algos:
            hash = getattr(hashlib, algo)(argument).hexdigest()
            items.append(ExtensionResultItem(icon='images/icon.png', name=hash, description=algo, highlightable=False, on_enter=CopyToClipboardAction(hash)))

        return RenderResultListAction(items)

if __name__ == '__main__':
    HashExtension().run()
