import datetime
import wifilists
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
        networks= wifilists.listavailable()
        saved=networks[0]
        available=networks[1]
        if len(saved)>0:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='Saved and Available',
                    description="Click to Connect",
                    on_enter=ExtensionCustomAction({'item': 'Null'}, keep_app_open=False)
                ))
        for i in saved:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name=f'{saved[i][0]},{i},{saved[i][1]}',
                    on_enter=ExtensionCustomAction({'item': i}, keep_app_open=False)
                ))
        if len(available)>0:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='Available',
                    description="Click to Connect",
                    on_enter=ExtensionCustomAction({'item': 'Null'}, keep_app_open=False)
                ))
        for i in available:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name=f'{available[i][0]},{i},{available[i][1]}',
                    on_enter=ExtensionCustomAction({'item': i}, keep_app_open=False)
                ))

        
        return RenderResultListAction(items[:5])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        item = data.get('item')
        with open('/home/anishudupan/temppp/a.txt','a') as filee:
            filee.write(f"{datetime.datetime.today()} : got {item}\n")
            filee.close()

if __name__ == '__main__':
    mainfn().run()
    


