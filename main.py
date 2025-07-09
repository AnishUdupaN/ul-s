from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
class ClipboardHistoryExtension(Extension):
    def __init__(self):
        super(ClipboardHistoryExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())



class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = ['apple','ball','cat']
        for i in range(len(items)):
            items.append(ExtensionResultItem(
                icon=os.path.join(os.getcwd(),'images/icon.png'),
                name=items[i],
                description="Click to Open",
                on_enter=RunScriptAction(f'xdg-open "www.{lines[i]}.com"', [])
            ))
        return RenderResultListAction(items[:5])

if __name__ == '__main__':
    ClipboardHistoryExtension().run()
    

    
"""
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction


class ClipboardHistoryExtension(Extension):

    def __init__(self):
        super(ClipboardHistoryExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        query = event.get_argument() or ""
        num_entries = int(extension.preferences.get('num_entries', 10))

        icon_path = 'images/cliplight.png'
        
        items.append(ExtensionResultItem(
            icon=icon_path,
            name=query,
            description="Press Enter to copy",
            on_enter=CopyToClipboardAction(query)
        ))
        return RenderResultListAction(items[:num_entries])


if __name__ == '__main__':
    ClipboardHistoryExtension().run()
"""
