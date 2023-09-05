import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


# Set the Kivy window size (optional)
# from kivy.config import Config
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '200')

class SimpleKivyApp(App):
    def build(self):
        self.title = 'Calculator'
        
        # Create a vertical BoxLayout
        AllLay = BoxLayout(orientation='vertical')
        layout = GridLayout(cols = 4, padding=20, spacing=10)
        
        # Create a label
        self.screen = Label(text='')

        # Create a button

        reset = Button(text='AC')
        reset.bind(on_press=self.reset_screen)

        one = Button(text='1')
        one.bind(on_press=self.on_button_click1)

        two = Button(text='2')
        two.bind(on_press=self.on_button_click2)

        three = Button(text='3')
        three.bind(on_press=self.on_button_click3)

        four = Button(text='4')
        four.bind(on_press=self.on_button_click4)
        
        five = Button(text='5')
        five.bind(on_press=self.on_button_click5)

        six = Button(text='6')
        six.bind(on_press=self.on_button_click6)

        seven = Button(text='7')
        seven.bind(on_press=self.on_button_click7)

        eight = Button(text='8')
        eight.bind(on_press=self.on_button_click8)

        nine = Button(text='9')
        nine.bind(on_press=self.on_button_click9)

        zero = Button(text='0')
        zero.bind(on_press=self.on_button_click0)

        plus = Button(text='+')
        plus.bind(on_press=self.on_button_click_plus)

        minus = Button(text='-')
        minus.bind(on_press=self.on_button_click_minus)

        mult = Button(text='x')
        mult.bind(on_press=self.on_button_click_mult)

        div = Button(text='/')
        div.bind(on_press=self.on_button_click_div)

        equal = Button(text='=')
        equal.bind(on_press=self.on_button_click_end)


        # Add the label and button to the layout
        layout.add_widget(one)
        layout.add_widget(two)
        layout.add_widget(three)
        layout.add_widget(reset)
        layout.add_widget(four)
        layout.add_widget(five)
        layout.add_widget(six)
        layout.add_widget(plus)
        layout.add_widget(seven)
        layout.add_widget(eight)
        layout.add_widget(nine)
        layout.add_widget(minus)
        layout.add_widget(zero)
        layout.add_widget(mult)
        layout.add_widget(div)
        layout.add_widget(equal)

        AllLay.add_widget(self.screen)
        AllLay.add_widget(layout)

        return AllLay

    def on_button_click1(self, instance): 
        self.screen.text += '1'
    
    def on_button_click2(self, instance): self.screen.text += '2'

    def on_button_click3(self, instance): self.screen.text += '3'

    def on_button_click4(self, instance): self.screen.text += '4'

    def on_button_click5(self, instance): self.screen.text += '5'

    def on_button_click6(self, instance): self.screen.text += '6'

    def on_button_click7(self, instance): self.screen.text += '7'

    def on_button_click8(self, instance): self.screen.text += '8'

    def on_button_click9(self, instance): self.screen.text += '9'

    def on_button_click0(self, instance): self.screen.text += '0'

    def on_button_click_plus(self, instance): self.screen.text += '+'

    def on_button_click_minus(self, instance): self.screen.text += '-'

    def on_button_click_mult(self, instance): self.screen.text += 'x'

    def on_button_click_div(self, instance): self.screen.text += '/'

    def on_button_click_end(self, instance): 
        txt = self.screen.text
        nums = '1234567890'
        sum = 0
        min = 0
        mult = 0
        div = 0
        if txt:
            min = int(txt[0])
            mult = int(txt[0])
            div = int(txt[0])
            if txt[1] == '+': 
                sum = (int(txt[0])+ int(txt[2]))
                self.screen.text += f' = {sum}'
            if txt[1] == '-': 
                min = (int(txt[0])- int(txt[2]))
                self.screen.text += f' = {min}'
            if txt[1] == 'x': 
                mult = (int(txt[0])* int(txt[2]))
                self.screen.text += f' = {mult}'
            if txt[1] == '/': 
                if int(txt[2]) == 0: self.screen.text = 'not able to divide by zero'
                else:
                    div = (int(txt[0])/ int(txt[2]))
                    self.screen.text += f' = {div}'
            # for char in txt:
            #     for num in nums:
            #         if char == num: sum+= int(char)
        else: self.screen.text = 'no equasion'

    def on_button_click_eq(self,instance):
        txt = self.screen.text
        nums = '1234567890'
        for char in txt:
            i=0
            n1 = int(txt[i])
            n2 = 0
            for num in nums:
                if txt[i+1] == num: n1 = int(txt[i]+txt[i+1]) 
                i+=1
            # if 1 and after 2 so 12.  go on to check if the following char is a number (if 1 and 2 and 3 so 123)
        sum = 0
        min = 0
        mult = 0
        div = 0
        if txt:
            min = int(txt[0])
            mult = int(txt[0])
            div = int(txt[0])
            if txt[1] == '+': 
                sum = (int(txt[0])+ int(txt[2]))
                self.screen.text += f' = {sum}'
            if txt[1] == '-': 
                min = (int(txt[0])- int(txt[2]))
                self.screen.text += f' = {min}'
            if txt[1] == 'x': 
                mult = (int(txt[0])* int(txt[2]))
                self.screen.text += f' = {mult}'
            if txt[1] == '/': 
                if int(txt[2]) == 0: self.screen.text = 'not able to divide by zero'
                else:
                    div = (int(txt[0])/ int(txt[2]))
                    self.screen.text += f' = {div}'
            
        else: self.screen.text = 'no equasion'

    def reset_screen(self, instance): self.screen.text = ''


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
