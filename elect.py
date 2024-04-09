import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from db import fetch_student_info, check_entry_exists, UpdateVotes
from kivy.uix.popup import Popup # UIX
from kivy.uix.label import Label # UIX
from kivy.uix.button import Button # UIX
from kivy.uix.boxlayout import BoxLayout # UIX
from kivy.uix.togglebutton import ToggleButton
import mysql.connector
# gr number not found/invalid
# already voted
#Defining diff screens
class GrNo(Screen):
    pass

class Heads(Screen):
    pass

class AgniSr(Screen):
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

    def fetch_info(self, final_num): #also checks the house
        fetch_student_info(final_num)

    

    def voteUpdateB(self):
        UpdateVotes(self.options_instance.selectBoys)

    def voteUpdateG(self):
        UpdateVotes(self.options_instance.selectGirls)
        print("Uploaded to DB")




    def CheckGr(self):
        validity = check_entry_exists(database.final_num)
        if validity is not None:
            App.get_running_app().root.current = 'Heads'
            print(f"from if statement {database.final_num}")
        else:
            # Creating the close button
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='The entered GR number is invalid.'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Invalid GR Number', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
             
class ScreenCases:
    def ScreenSwitch(self):
        # Call the fetch_student_info function to get the house information
        house = fetch_student_info(database.final_num)  # Assuming database.final_num is defined elsewhere
        if house is not None:  # Check if house information is retrieved successfully
            if house == 'AGNI':
                App.get_running_app().root.current = 'AgniSr'
            else:
                print("House is not Agni")
                print(house)
        else:
            print("Failed to fetch house information.")


class PopUps():
    def GrNoPopUp():
        pass

class Options():
    def __init__(self, options_instance):
        self.options_instance = options_instance
        self.selectBoys = None
        self.selectGirls = None

    def HandleOptionB(self, option_id, state):
        if state == 'down':
            if self.selectBoys == option_id:  # If the option is already selected
                self.selectBoys = None  # Deselect it
                print("Deselected option for boys:", option_id)
            else:
                self.selectBoys = option_id  # Otherwise, select it
                print("Selected option for boys:", option_id)
        else:  # Handle deselection when the button is released
            if self.selectBoys == option_id:  # If the option was previously selected
                self.selectBoys = None  # Deselect it
                print("Deselected option for boys:", option_id)
            
    def HandleOptionG(self, option_id, state): 
        if state == 'down':
            if self.selectGirls == option_id:  # If the option is already selected
                self.selectGirls = None  # Deselect it
                print("Deselected option for Girls:", option_id)
            else:
                self.selectGirls = option_id  # Otherwise, select it
                print("Selected option for Girls:", option_id)
        else:  # Handle deselection when the button is released
            if self.selectGirls == option_id:  # If the option was previously selected
                self.selectGirls = None  # Deselect it
                print("Deselected option for Girls:", option_id)


class Cool(App):
    def build(self):
        self.gr_number = None
        screen_manager = ScreenManager()
        self.database = database()  # Create an instance of the database class
        self.options = self.database.options_instance  # Access the Options instance from the database
        self.screen_cases = ScreenCases()
        return kv


    def handle_button(self, gr_input):
        self.database.StoreGr(gr_input)
        self.database.CheckGr()
    



if __name__ == '__main__':
    Cool().run()
