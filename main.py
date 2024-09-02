from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Pressione o botão para somar {} + {}".format(1, 1))
        self.button = Button(text="Calcular", on_press=self.calculate)
        
        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout
    
    def calculate(self, instance):
        result = 1 + 1
        self.label.text = "1 + 1 = {}".format(result)

if __name__ == '__main__':
    MyApp().run()