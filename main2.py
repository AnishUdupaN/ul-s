import datetime
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
class mainfn(Extension):
    def __init__(self):
        super(mainfn, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items=[]
        lstt = ['apple','ball','cat']
        for i in range(len(lstt)):
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name=lstt[i],
                description="Click to Open",
                on_enter=ExtensionCustomAction({'item': lstt[i]}, keep_app_open=False)
            ))
    
        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name="Hello",
            on_enter=ExtensionCustomAction({'item': "Hello"}, keep_app_open=False)
        ))

        return RenderResultListAction(items[:5])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        item = data.get('item')
        """
        with open('/home/anishudupan/temppp/a.txt','a') as filee:
            filee.write(f"{datetime.datetime.today()} : got {item}\n")
            filee.close()
        """
if __name__ == '__main__':
    mainfn().run()
    


