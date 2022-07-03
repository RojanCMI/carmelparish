from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.videoplayer import VideoPlayer

class WindowManager(ScreenManager):
    pass

class ScrollIcon(ScrollView):
    # pass y-move event to parent instead of stopping
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False

class ToolbarNavigate(Screen):
    def __init__(self,**kwargs):
        super().__init__()
        Clock.schedule_interval(self.slide_next, 7)

    def slide_next(self, *args):
        self.ids.carousel.load_next()

class Vidi(Screen):
    def on_enter(self, *args):
        self.video = VideoPlayer(source="faith.mp4", size_hint=(1, .89))
        self.video.state = 'play'
        self.add_widget(self.video)

    def on_leave(self, *args):
        self.video.state = 'stop'

class Vidii(Screen):
    def on_enter(self, *args):
        self.video = VideoPlayer(source="faith.mp4")
        self.video.state = 'play'
        self.add_widget(self.video)

    def on_leave(self, *args):
        self.video.state = 'stop'

class Carmel(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen_manager = WindowManager()
        screen_manager.add_widget(ToolbarNavigate(name='toolbar_nav'))
        screen_manager.add_widget(Vidi(name='vidi'))
        screen_manager.add_widget(Vidii(name='vidii'))
        return screen_manager

if __name__ == '__main__':
    Carmel().run()
