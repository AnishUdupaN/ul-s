import datetime
import wifilists
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

#network does not connect to unsaved secure networks

class mainfn(Extension):
    def __init__(self):
        super(mainfn, self).__init__()
        print('Initialized\n\n')
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items=[]
        print('On Event\n\n')
        saved=wifilists.listavailable()
        for i in saved:
            lockk='nolock' if saved[i][1]=="" else 'lock'
            items.append(ExtensionResultItem(
                    icon=f'./images/{lockk}/{saved[i][0]}bars.png',
                    name=i,
                    on_enter=ExtensionCustomAction({'SSID': i}, keep_app_open=True)
                ))
        itemsno=len(saved)
        return RenderResultListAction(items[:itemsno])
        

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        """
        Main Logic:
        if IsSavedNetwork:
            connect()
            if ConnectionSuccessful:
                print("Success")
            else:
                print("Failure")
        else:
            connect()
            if ConnectionSuccessful:
                print("Success")
            else:
                print("Failure")
        """
        items=[]
        print('EnterEventListener')
        data = event.get_data()
        #saved network
        a=wifilists.Connect(data['SSID'])
        if a==True:
            #connection success
            items.append(ExtensionResultItem(
                icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                name=f'Connected Successfully to {data['SSID']}!',
                on_enter=DoNothingAction()
            ))
        else:
            #connection failure
            items.append(ExtensionResultItem(
                icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                name='Connection Failure',
                on_enter=DoNothingAction()
            ))
        return RenderResultListAction(items[:1])
    
        

if __name__ == '__main__':
    mainfn().run()
    


