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
   
        md5Hash = hashlib.md5(event.get_argument().encode('utf-8')).hexdigest()
        sha1Hash = hashlib.sha1(event.get_argument().encode('utf-8')).hexdigest()
        sha224Hash = hashlib.sha224(event.get_argument().encode('utf-8')).hexdigest()
        sha256Hash = hashlib.sha256(event.get_argument().encode('utf-8')).hexdigest()
        sha512Hash = hashlib.sha512(event.get_argument().encode('utf-8')).hexdigest()
        
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=md5Hash,
                                         description='md5',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(
                                             md5Hash)
                                         ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                          name=sha1Hash,
                                          description='sha1',
                                          highlightable=False,
                                          on_enter=CopyToClipboardAction(
                                              sha1Hash)
                                          ))


        items.append(ExtensionResultItem(icon='images/icon.png',
                                          name=sha224Hash,
                                         description='sha224',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(
                                             sha224Hash)
                                         ))
        
        items.append(ExtensionResultItem(icon='images/icon.png',
                                          name=sha256Hash,
                                          description='sha256',
                                          highlightable=False,
                                          on_enter=CopyToClipboardAction(
                                              sha256Hash)
                                          ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=sha512Hash,
                                         description='sha512',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(
                                              sha512Hash)
                                         ))

        return RenderResultListAction(items)

if __name__ == '__main__':
   HashExtension().run()
