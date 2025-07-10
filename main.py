from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
import wifilists


class MainFn(Extension):
    def __init__(self):
        super(MainFn, self).__init__()
        print('Initialized\n\n')
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateEventListener())


class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        extension.preferences.update(event.preferences)


class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension):
        extension.preferences[event.id] = event.new_value


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        print('On Event\n\n')
        saved = wifilists.listavailable()
        print(saved.items())
        for i in saved.items():
            lockk = 'nolock' if i[1][1] == "" else 'lock'
            items.append(ExtensionResultItem(
                    icon=f'./images/{lockk}/{i[1][0]}bars.png',
                    name=i[0],
                    on_enter=ExtensionCustomAction({'SSID': i[0]}, keep_app_open=True)
                ))
        num_entries = int(extension.preferences.get('num_entries', 10))

        return RenderResultListAction(items[:num_entries])


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        print('EnterEventListener')
        data = event.get_data()
        a = wifilists.Connect(data['SSID'])
        if a is True:
            # connection success
            items.append(ExtensionResultItem(
                icon='./images/icon.png',
                name=f'Connected Successfully to {data['SSID']}!',
                on_enter=DoNothingAction()
            ))
        else:
            # connection failure
            items.append(ExtensionResultItem(
                icon='./images/icon.png',
                name='Connection Failure',
                on_enter=DoNothingAction()
            ))
        return RenderResultListAction(items[:1])


if __name__ == '__main__':
    MainFn().run()
