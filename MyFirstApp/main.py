#  This is an application to show a simple static page
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix import screen
from kivymd.uix import button
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton,MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog

# Also I have added my name to the first application so the App will be called as AbhiAPP
class AbhiAPPApp(MDApp):

    def build(self):
        self.theme_cls.theme_style="Dark"
        screen = Screen()
        lbl = MDLabel(text="Hello Abhi Welcome to this app",halign="center",pos_hint={'center_y':0.9})
        lbl2 = MDLabel(text="This app doesn't have any use but",halign="center",pos_hint={'center_y':0.8})
        lbl3 = MDLabel(text="It's still the app which can be there",halign="center",pos_hint={'center_y':0.7})
        lbl4 = MDLabel(text="In most of the android devices.",halign="center",pos_hint={'center_y':0.6})
        icon = MDFloatingActionButton(icon='language-python',pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.python_lang)
        lbl5 = MDLabel(text="Made By Abhinand.",halign="center",pos_hint={'center_y':0.1},theme_text_color="Primary")
        screen.add_widget(icon)
        screen.add_widget(lbl)
        screen.add_widget(lbl2)
        screen.add_widget(lbl3)
        screen.add_widget(lbl4)
        screen.add_widget(lbl5)
        return screen
    
    def python_lang(self,obj):
        # I also have added a dialog box here this will be presented when Python Logo is pressed
        close_btn = MDFlatButton(text="Close",on_release=self.close_dlg)
        self.dlg = MDDialog(title="Hey Friend,",text="This App is made with help of using KivyMD",size_hint=(0.5,1),buttons=[close_btn])
        self.dlg.open()


    def close_dlg(self,obj):
        self.dlg.dismiss()

AbhiAPPApp().run()

# I am grateful to KivyMD,Python3,Buildozer for providing their platform for creation of this application,

    