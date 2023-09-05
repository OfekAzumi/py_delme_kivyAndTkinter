from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


class ColorChangeApp(App):
    def build(self):
        # Create a BoxLayout as the root widget
        layout = BoxLayout(orientation='vertical')

        # Set the background color of the layout
        with layout.canvas.before:
            Color(0.2, 0.7, 0.2, 1)  # RGBA color values (red, green, blue, alpha)
            self.rect = Rectangle(size=(layout.width, layout.height))

        return layout

if __name__ == '__main__':
    ColorChangeApp().run()