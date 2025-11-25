import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class contador_app(App):
    # Propiedad para mostrar el número de clics en la interfaz
    click_display_count = NumericProperty(0)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Etiqueta
        self.label = Label(text="Pulsa el botón para contar clicks")
        layout.add_widget(self.label)

        # Botón
        self.button = Button(text=f"Clicks: {self.click_display_count}",
                             font_size=50)
        self.button.bind(on_press=self.on_button_press)
        layout.add_widget(self.button)

        # Para actualizar el texto cuando cambie el contador
        self.bind(click_display_count=self.update_button_text)

        return layout

    def update_button_text(self, instance, value):
        """Actualiza el texto del botón con el número actual de clics."""
        self.button.text = f"Clicks: {value}"

    def on_button_press(self, instance):
        """Incrementa el contador visual."""
        self.click_display_count += 1

if __name__ == '__main__':
    contador_app().run()
