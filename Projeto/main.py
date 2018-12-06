from kivy.app        import App
from kivy.uix.widget import Widget
from kivy.config     import Config
from telas           import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Carrega nosso arquivo de configurações
Config.read("config.ini")

# Cria nosso Gerenciador de Telas
screen_manager = ScreenManager()

class MusicApp(App):

    def build(self):


        # Cria a Tela do Player
        tela_player = TelaPlayer(name="Player")

        # Adiciona as telas ao nosso gerenciador
        screen_manager.add_widget(TelaSelecao(name='Selecao'))
        screen_manager.add_widget(tela_player)
        screen_manager.add_widget(TelaHistorico(name='Historico'))

        return screen_manager

if __name__ == '__main__':
    MusicApp().run()
