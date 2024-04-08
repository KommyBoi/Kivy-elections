import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from db import fetch_student_info, check_entry_exists, UpdateVotes
import mysql.connector
# gr number not found/invalid
# already voted
#Defining diff screens
class GrNo(Screen):
    pass

class Heads(Screen):
    pass

class InvalidGr(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('screen.kv')

# class MyElect(Widget):
#     pass

class database():
    def __init__(self):
        self.final_num = None
        self.options_instance = Options(self)
    def StoreGr(self, gr_input):
        app = App.get_running_app()
        app.gr_number = int(gr_input.text)
        database.final_num = app.gr_number
        print(database.final_num)

    def fetch_info(self, final_num):
        fetch_student_info(final_num)
    

    def voteUpdateB(self):
        UpdateVotes(self.options_instance.selectBoys)

    def voteUpdateG(self):
        UpdateVotes(self.options_instance.selectGirls)


    def CheckGr(self):
        validity = check_entry_exists(database.final_num)
        if validity is not None:  # Assuming final_num is set somewhere in your application
            App.get_running_app().root.current = 'Heads'  # Switch to 'Heads' screen
            print(f"from if statement {database.final_num}" )  
        else:
            App.get_running_app().root.current = 'InvalidGr'
            print(f"from else statement {database.final_num}")    
             
class Options():
    def __init__(self, options_instance):
        self.options_instance = options_instance
        self.selectBoys = None
        self.selectGirls = None

    def HandleOptionB(self, option_id, state):
        if state == 'down':
            self.selectBoys = option_id
            print("Selected option for boys:", self.selectBoys)

    def HandleOptionG(self, option_id, state): 
        if state == 'down':
            self.selectGirls = option_id
            print("Selected option for girls:", self.selectGirls)


class Cool(App):
    def build(self):
        self.gr_number = None
        screen_manager = ScreenManager()
        self.database = database()  # Create an instance of the database class
        self.options = self.database.options_instance  # Access the Options instance from the database
        return kv


    def handle_button(self, gr_input):
        self.database.StoreGr(gr_input)
        self.database.CheckGr()


if __name__ == '__main__':
    Cool().run()
