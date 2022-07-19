from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class SoundPlayer(Widget):
    vl = 0.1
    sn = 1
    increase = 0.5
    def play_button(self):
        self.sound = SoundLoader.load('test.mp3')
        if self.sound:
            print("play1")
            self.sound.play()
            print("sound found at " + str(self.sound.source))
            print("Sound is %.3f seconds" % self.sound.length)
        if self.sound.volume == float(0.5):
            self.volume_button()

    def play_button2(self):
        self.sound = SoundLoader.load('sound.wav')
        if self.sound:
            print("playing2..")
            self.sound.play()
            print("sound found at " + str(self.sound.source))
            print("Sound is %.3f seconds" % self.sound.length)
            #self.sound.volume = 0.1
        if self.sound.volume == 0.1:
            self.volume_increase_button()

    def volume_button(self):
        self.sound.volume = self.vl
        print("0.1")

    def volume_increase_button(self):
        self.sound.volume = self.increase
        print ("0.5")
    
    def stop_button(self):
        print("song stop")
        self.sound.stop()
    

class MyApp(App):
    def build(self):
        return SoundPlayer()

MyApp().run()