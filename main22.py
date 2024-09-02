from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class calculadora(App):
    def build(self):
        self.operacao = ''
        self.num1 = ''
        self.num2 = ''

        layout = BoxLayout(orientation='vertical')

        self.display = TextInput(font_size=40, readonly=True, multiline=False)
        layout.add_widget(self.display)

        botoes_layout = BoxLayout(orientation='horizontal')

        botoes = [
            ('7', self.add_digit),
            ('8', self.add_digit),
            ('9', self.add_digit),
            ('/', self.add_operator),
            ('4', self.add_digit),
            ('5', self.add_digit),
            ('6', self.add_digit),
            ('*', self.add_operator),
            ('1', self.add_digit),
            ('2', self.add_digit),
            ('3', self.add_digit),
            ('-', self.add_operator),
            ('C', self.clear_display),
            ('0', self.add_digit),
            ('=', self.calculate),
            ('+', self.add_operator),
        ]

        for texto, acao in botoes:
            botao = Button(text=texto, on_press=acao)
            botoes_layout.add_widget(botao)

        layout.add_widget(botoes_layout)

        return layout
    
    def add_digit(self, instance):
        self.display.text += instance.text

    def add_operator(self, instance):
        if not self.operacao:
            self.num1 = self.display.text
            self.operacao = instance.text
            self.display.text = ''

    def clear_display(self, instance):
        self.display.text = ''
        self.operacao = ''
        self.num1 = ''
        self.num2 = ''

    def calculate(self, instance):
        if self.num1 and self.operacao and self.display.text:
            self.num2 = self.display.text
            try:
                resultado = eval(self.num1 + self.operacao + self.num2)
                self.display.text = str(resultado)
                self.operacao = ''
                self.num1 = ''
                self.num2 = ''
            except ZeroDivisionError:
                self.display.text = 'Erro: divisão por zero'
                self.operacao = ''
                self.num1 = ''
                self.num2 = ''


if __name__ == '__main__':
    calculadora().run()
