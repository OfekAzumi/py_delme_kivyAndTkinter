import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle


# Set the Kivy window size (optional)
# from kivy.config import Config
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '200')

class SimpleKivyApp(App):
    def build(self):
        self.title = 'Simple Kivy App'
        
        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Create a label
        self.label = Label(text='Hello, Kivy!')

        # Create a button
        button = Button(text='Blue')
        button.bind(on_press=self.on_button_click)

        button2 = Button(text='Green')
        button2.bind(on_press=self.on_button_click2)

        button3 = Button(text='Red')
        button3.bind(on_press=self.on_button_click3)


        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)
        layout.add_widget(button2)

        return layout

    def on_button_click(self, instance):
        # Change the label text when the button is clicked
        self.label.text = 'Button Clicked!'
    
    def on_button_click2(self, instance):
        # Change the label text when the button is clicked
        self.label.text = 'Does it overlap?!'

    def on_button_click3(self, instance):
        # Change the label text when the button is clicked
        self.label.text = 'Does it overlap?!'


# class ColorChangeApp(App):
#     def build(self):
#         # Create a BoxLayout as the root widget
#         layout = BoxLayout(orientation='vertical', height = '200px')

#         # Set the background color of the layout
#         with layout.canvas.before:
#             Color(0.2, 0.7, 0.2, 1)  # RGBA color values (red, green, blue, alpha)
#             self.rect = Rectangle(size=(layout.width, layout.height))

#         return layout
    
if __name__ == '__main__':
    SimpleKivyApp().run()
