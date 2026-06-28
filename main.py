from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from datetime import datetime

class LotteryScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        header = Label(text='DỰ ĐOÁN XỔ SỐ', font_size=22, bold=True, size_hint_y=None, height=60)
        self.add_widget(header)

        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=180)
        input_layout.add_widget(Label(text='Giải ĐB hôm qua:'))
        self.special_input = TextInput(hint_text='Ví dụ: 71294', multiline=False, input_filter='int')
        input_layout.add_widget(self.special_input)
        input_layout.add_widget(Label(text='Ngày (dd/mm/yyyy):'))
        self.date_input = TextInput(hint_text=datetime.now().strftime('%d/%m/%Y'), multiline=False)
        input_layout.add_widget(self.date_input)
        input_layout.add_widget(Label(text='Giờ (1-12):'))
        self.hour_input = TextInput(hint_text='7', multiline=False, input_filter='int')
        input_layout.add_widget(self.hour_input)
        self.add_widget(input_layout)

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_calc = Button(text='TÍNH BỘ SỐ', background_color=(0.2, 0.6, 1, 1))
        btn_calc.bind(on_press=self.calculate_prediction)
        btn_layout.add_widget(btn_calc)
        self.add_widget(btn_layout)

        scroll = ScrollView()
        self.result_label = Label(text='Nhấn "TÍNH BỘ SỐ" để bắt đầu...', size_hint_y=None, halign='left', valign='top')
        self.result_label.bind(texture_size=self.result_label.setter('size'), width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        scroll.add_widget(self.result_label)
        self.add_widget(scroll)

    def calculate_prediction(self, instance):
        try:
            special = int(self.special_input.text or "71294")
            hour = int(self.hour_input.text or "7")
            core1 = int(str(int(special * 0.618))[-2:]) 
            core2 = int(str(int(special * 1.618))[-2:])
            core3 = int(str(int(special * 2.618))[-2:])
            maihoa = (special % 8) + (hour % 8) + 1
            if maihoa > 8: maihoa = 8
            two_digit = [f"{core1:02d}", f"{core2:02d}", f"{(core1 + core2) % 100:02d}"]
            three_digit = [f"{core1}{core2}{maihoa}", f"{core2}{core1}{core3%10}", f"{core1}{core3}{core2%10}"]
            self.result_label.text = f"✅ KẾT QUẢ NGÀY {self.date_input.text or datetime.now().strftime('%d/%m/%Y')}\n\n🌟 HẠT NHÂN CHÍNH:\n• Fibonacci: {core1:02d}, {core2:02d}, {core3:02d}\n• Mai Hoa: {maihoa}\n\n📌 BỘ ĐỀ XUẤT 2 CON:\n{', '.join(two_digit)}\n\n📌 BỘ ĐỀ XUẤT 3 CON:\n{', '.join(three_digit)}"
        except Exception as e:
            self.result_label.text = f"Lỗi: {str(e)}\nVui lòng nhập số hợp lệ!"

class LotteryApp(App):
    def build(self):
        return LotteryScreen()

if __name__ == '__main__':
    LotteryApp().run()
