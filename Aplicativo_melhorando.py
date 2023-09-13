from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from datetime import datetime

class NameListApp(App):
    def build(self):
        self.names = []

        layout = BoxLayout(orientation='vertical')

        self.name_input = TextInput(hint_text='Nome')
        add_button = Button(text='Adicionar Nome', on_release=self.add_name)
        access_button = Button(text='Acessar Nomes', on_release=self.access_names)
        edit_button = Button(text='Editar Nomes', on_release=self.edit_names)
        time_button = Button(text='Hora Atual', on_release=self.show_current_time)

        layout.add_widget(self.name_input)
        layout.add_widget(add_button)
        layout.add_widget(access_button)
        layout.add_widget(edit_button)
        layout.add_widget(time_button)

        self.output_label = Label(text='',halign='center', valign='middle')
        layout.add_widget(self.output_label)

        return layout

    def build_Name(self, display_layout=None):

        self.display_screen = Screen(name='display')
        diplay_layout = BoxLayout(orientation='vertical')
        self.display_label = Label(text='', halign='center',valign='middle')
        diplay_layout.add_widget(self.display_label)
        back_button = Button(text='Voltar', on_release=self.back_to_main)
        display_layout.add_widget(back_button)
        self.display_screen.add_widget(display_layout)

        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.display_screen)
        return self.sm

    def add_name(self, instance):
        name = self.name_input.text.strip()
        if name:
            self.names.append(name)
            self.save_to_txt(name)
            self.name_input.text = ''

    def save_to_txt(self, name):
        with open('names.txt', 'a') as file:
            file.write(name + '\n')

    def access_names(self, instance):
        names_displat = '\n'.join(self.names)
        self.output_label.text = names_displat

    def edit_names(self, instance):
        # implementando a funcionalidade de edição aqui
        pass

    def show_current_time(self, instance):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.output_label.text = f'Hora atual: {current_time}'

if __name__ == '__main__':
    NameListApp().run()
