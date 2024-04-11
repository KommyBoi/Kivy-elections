import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from db import fetch_student_info, check_entry_exists, UpdateVotes
from kivy.uix.togglebutton import ToggleButton

from kivy.uix.popup import Popup #UIX
from kivy.uix.label import Label #UIX
from kivy.uix.button import Button #UIX
from kivy.uix.boxlayout import BoxLayout #UIX
from kivy.uix.togglebutton import ToggleButton #UIX
from kivy.config import Config
import mysql.connector
# gr number not found/invalid
# already voted
#Defining diff screens

Config.set('graphics', 'width', '1600')
Config.set('graphics', 'height', '900')

class GrNo(Screen):
    pass

class Heads(Screen):
    pass

class VHeads(Screen):
    pass

class JHeads(Screen):
    pass

class InvalidGr(Screen):
    pass

class AgniSr(Screen):
    pass

class AgniJr(Screen):
    pass

class PrithviSr(Screen):
    pass

class PrithviJr(Screen):
    pass

class SuryaSr(Screen):
    pass    

class SuryaJr(Screen):
    pass

class VarunSr(Screen):
    pass

class VarunJr(Screen):
    pass

class EndScreen(Screen):
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

    def PopUpH(self):
        if self.selectBoys and self.selectGirls != None:
            App.get_running_app().root.current = 'VHeads'
            self.selectBoys = None
            self.selectGirls = None
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Headboy and Headgirl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")

    def PopUpVH(self):
        if self.selectBoys and self.selectGirls != None:
            App.get_running_app().root.current = 'JHeads'
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Vice Headboy and Vice Headgirl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
        self.SelectBoys = None
        self.SelectGirls = None

    def PopUpV(self):
        if self.selectBoys and self.selectGirls != None:
            App.get_running_app().root.current = 'VarunJr'
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Sr. Sports captain boy and girl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
        self.SelectBoys = None
        self.SelectGirls = None

    def PopUpP(self):
        if self.selectBoys and self.selectGirls != None:
            App.get_running_app().root.current = 'PrithviJr'
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Sr. Sports captain boy and girl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
        self.SelectBoys = None
        self.SelectGirls = None

    def PopUpA(self):
        if self.selectBoys and self.selectGirls != None:
            App.get_running_app().root.current = 'AgniJr'
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Sr. Sports captain boy and girl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
        self.SelectBoys = None
        self.SelectGirls = None

    def PopUpS(self):
        if self.selectBoys and self.selectGirls != None:
            App.get_running_app().root.current = 'SuryaJr'
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Sr. Sports captain boy and girl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
        self.SelectBoys = None
        self.SelectGirls = None


    def PopUpJH(self):
        house_switch = fetch_student_info(database.final_num)
        if self.selectBoys and self.selectGirls != None:
            if house_switch == 'Agni':
                App.get_running_app().root.current = 'AgniSr'
            elif house_switch == 'Varun':
                App.get_running_app().root.current = 'VarunSr'
            elif house_switch == 'Surya':
                App.get_running_app().root.current = 'SuryaSr'
            elif house_switch == 'Prithvi':
                App.get_running_app().root.current = 'PrithviSr'
            self.selectBoys = None
            self.selectGirls = None
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Jr. Headboy and Jr. Headgirl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")

    def EndScreen(self):
        if self.selectBoys and self.selectGirls != None:
            close_button = Button(text='CLOSE APP')
            close_button.bind(on_release=lambda instance: self.CloseApp())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Your votes have been recorded!'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Voting complete', content=popup_content,
                        size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
        else: 
            close_button = Button(text='CLOSE')
            close_button.bind(on_release=lambda instance: popup.dismiss())

            # Creating and showing the popup
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text='Please select Jr. Sports captain boy and girl'))
            popup_content.add_widget(close_button)

            popup = Popup(title='Options not selected', content=popup_content,
                        size_hint=(None, None), size=(400, 200))
            popup.open()
            print(f"from else statement {database.final_num}")
    def CloseApp(self):
        App.get_running_app().stop()


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
