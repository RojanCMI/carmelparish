from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class ToolbarNavigate(Screen):
    def __init__(self,**kwargs):
        super().__init__()

class Carmel(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen_manager = WindowManager()
        screen_manager.add_widget(ToolbarNavigate(name='toolbar_nav'))
        return screen_manager

if __name__ == '__main__':
    Carmel().run()
