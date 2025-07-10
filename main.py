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
        networks= wifilists.listwifi()
        saved=networks[0]
        available=networks[1]
        #saved
        #saved=[1,2,3,4]
        if len(saved)>0:
            items.append(ExtensionResultItem(
                    icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                    name='Saved and Available',
                    description="Click to Connect",
                    on_enter=DoNothingAction()
                ))
        
        for i in saved:
            items.append(ExtensionResultItem(
                    icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                    name=f'{saved[i][0]},{i},{saved[i][1]}',
                    on_enter=ExtensionCustomAction({'SSID': i,'SECURITY':saved[i][1],'SAVED':True}, keep_app_open=True)
                ))
        #not saved
        if len(available)>0:
            items.append(ExtensionResultItem(
                    icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                    name='Available',
                    description="Cannot Connect Here",
                    on_enter=DoNothingAction()
                ))
        for i in available:
            items.append(ExtensionResultItem(
                    icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                    name=f'{available[i][0]},{i},{available[i][1]}',
                    on_enter=ExtensionCustomAction({'SSID': i,'SECURITY':available[i][1],'SAVED':False}, keep_app_open=True)
                ))
        itemsno=len(saved)+len(available)+2
        return RenderResultListAction(items[:itemsno])
        
        return RenderResultListAction(items[:1])


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        items=[]
        print('EnterEventListener')
        data = event.get_data()
    
        if data['SAVED']==True:
            #saved network
            a=wifilists.SavedConnect(data['SSID'])
            with open('/home/anishudupan/temppp/a.txt','a') as filee:
                filee.write(f"{datetime.datetime.today()} : Connection with {data['SSID']} with status {a}\n")
                filee.close()
            if a==True:
                #connection success
                items.append(ExtensionResultItem(
                    icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                    name='Connected Successfully!',
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
        else:
            #unsaved network
            print(f"{data['SSID']}:{data['SECURITY']}\n")
            if data['SECURITY']=="":
                items.append(ExtensionResultItem(
                        icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                        name=f'Open Network',
                        on_enter=DoNothingAction()
                    ))
            else:
                items.append(ExtensionResultItem(
                        icon='/home/anishudupan/projects/ul-s/images/clipbrown.png',
                        name=f'Secure Network',
                        on_enter=DoNothingAction()
                    ))

            with open('/home/anishudupan/temppp/a.txt','a') as filee:
                filee.write(f"{datetime.datetime.today()} : In Else part {data['SSID']},{data['SECURITY']}\n")
                filee.close()
            return RenderResultListAction(items[:1])
            #wifilists.UnsavedConnect(data['SSID'])
    
        

if __name__ == '__main__':
    mainfn().run()
    


