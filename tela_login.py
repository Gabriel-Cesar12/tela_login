from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage

Window_size=(900,700)

class FloatApp(App):
    def build(self):
        Window.clearcolor=(0, 0, 0, 0)
        
        flo = FloatLayout()
        icon_login = AsyncImage(
            source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_xdBaKcH5J2x1p05Z1_ehDhk1RqaVZuFOvuk2bobgpg&s',
            pos=(325, 350),
            size_hint= (.4, .4)
            )

        flo.add_widget(icon_login)
        l1 = Button(
            text="Login", size_hint=(.2, .1),
            pos=(200, 350), color = [1,1,1,1]
        )

        flo.add_widget(l1)

        self.t1 = TextInput(size_hint=(.4, .1), pos=(400, 350))
        flo.add_widget(self.t1)
        
        l2 = Button(
            text="Senha", size_hint=(.2, .1),
            pos=(200, 250),color = [1,1,1,1]
        )
        
        flo.add_widget(l2)

        t2 = TextInput(
            multiline=True, size_hint=(.4, .1), pos=(400, 250)
        )

        flo.add_widget(t2)
        
        b1 = Button(
            text='Entrar', size_hint = (.3, .1),
            pos_hint = {'center_x':.5, 'center_y':.07},
            on_press = self.entrar
        )
        b2 = Button(
            text='Cadastrar', size_hint = (.3, .1),
            pos_hint = {'center_x':.5, 'center_y':.20},
            on_press = self.cadastrar
        )
        
        self.label_cadastrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )

        self.label_entrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )
        
        flo.add_widget(b1)
        flo.add_widget(b2)
        flo.add_widget(self.label_cadastrar)
        flo.add_widget(self.label_entrar)
        
        return flo

    def cadastrar(self, instance):
        login = self.t1.text
        mensagem = f'O Login {login} cadastrou minha fera!'
        self.label_cadastrar.text = mensagem
    
    def entrar(self, instance):
        login = self.t1.text
        mensagem = f'O login {login} Entrou minha fera!'
        self.label_cadastrar.text = mensagem

      
FloatApp().run()