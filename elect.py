import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('elect.kv')
class MyElect(Widget):
    pass

class Cool(App):
    def build(self):
        return MyElect()


if __name__ == '__main__':
    Cool().run()
