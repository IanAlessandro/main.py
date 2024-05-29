from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager

class FirstScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass


class RegisterScreen(MDScreen):
    pass

class MainScreen(MDScreen):
    pass

class Localizacao(MDScreen):
    pass

class Agendamento(MDScreen):
    pass

class Barbeiros(MDScreen):
    pass


class Servicos(MDScreen):
    pass


class App(MDApp, App):
    def build(self):
        Window.size = (360, 640)
        Builder.load_file(('main.kv'))
        self.theme_cls.primary_palette = 'Gray'
        screens = MDScreenManager()
        screens.add_widget(FirstScreen())
        screens.add_widget(LoginScreen())
        screens.add_widget(RegisterScreen())
        screens.add_widget(MainScreen())
        screens.add_widget(Localizacao())
        screens.add_widget(Agendamento())
        screens.add_widget(Barbeiros())
        screens.add_widget(Servicos())
        return screens
App().run()
