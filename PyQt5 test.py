import kivy
kivy.require("")
from kivy import*
class testApp(App):
    def build(self):
        return Label(text="TEST")

if __name__ == "__main__":
    testApp().run()