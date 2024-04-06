import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from db import fetch_student_info
import mysql.connector

#Defining diff screens
class GrNo(Screen):
    pass

class Heads(Screen):
    def StoreGr(self, gr_input):
        global final_num
        app = App.get_running_app()
        app.gr_number = int(gr_input.text)
        final_num = app.gr_number
        print(final_num)
        fetch_student_info(final_num)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('screen.kv')
# class MyElect(Widget):
#     pass

class database():
    def fetch_info(self, final_num):
        fetch_student_info(final_num)

class Cool(App):
    def build(self):
        self.gr_number = None
        self.database = database()
        return kv


if __name__ == '__main__':
    Cool().run()
