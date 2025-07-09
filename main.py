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
        networks= wifilists.listwifi()
        saved=networks[0]
        available=networks[1]
        #saved
        if len(saved)>0:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='Saved and Available',
                    description="Click to Connect",
                    on_enter=ExtensionCustomAction({'SSID': 'Null'}, keep_app_open=False)
                ))
        for i in saved:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name=f'{saved[i][0]},{i},{saved[i][1]}',
                    on_enter=ExtensionCustomAction({'SSID': i,'SECURITY':saved[i][1],'SAVED':True}, keep_app_open=True)
                ))
        #not saved
        if len(available)>0:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='Available',
                    description="Cannot Connect Here",
                    on_enter=ExtensionCustomAction({'SSID': 'Null'}, keep_app_open=False)
                ))
        for i in available:
            items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name=f'{available[i][0]},{i},{available[i][1]}',
                    on_enter=ExtensionCustomAction({'SSID': i,'SECURITY':saved[i][1],'SAVED':False}, keep_app_open=False)
                ))
        itemsno=len(saved)+len(available)+2
        return RenderResultListAction(items[:itemsno])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        items=[]
        data = event.get_data()
        if len(data)=1:
            return #do nothing ,should be replaced by do nothing API instead of custom instruction.
        else:
            if data['SAVED']==True:
                a=wifilists.SavedConnect(data['SSID'])
                with open('/home/anishudupan/temppp/a.txt','a') as filee:
                    filee.write(f"{datetime.datetime.today()} : Connection with {data['SSID']} with status {a}\n")
                    filee.close()
                if a==True:
                    items.append(ExtensionResultItem(
                        icon='images/icon.png',
                        name='Connected Successfully!',
                        on_enter=ExtensionCustomAction({'SSID': i,'SECURITY':saved[i][1],'SAVED':False}, keep_app_open=False) #do nothing action
                    ))
                else:
                    items.append(ExtensionResultItem(
                        icon='images/icon.png',
                        name='Connected Successfully!',
                        on_enter=ExtensionCustomAction({'SSID': i,'SECURITY':saved[i][1],'SAVED':False}, keep_app_open=False) #do nothing action
                    ))
                return RenderResultListAction(items[:1])
            else:
                with open('/home/anishudupan/temppp/a.txt','a') as filee:
                    filee.write(f"{datetime.datetime.today()} : In Else part {item}\n")
                    filee.close()
                #wifilists.UnsavedConnect(data['SSID'])
        

if __name__ == '__main__':
    mainfn().run()
    


