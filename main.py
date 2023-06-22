from kivy.app import App #Подключаем kivy
from kivy.uix.button import Button #Подключаем кнопки (Все виджеты в UIX)
from kivy.config import Config


Config.set('graphics','resizable','0'); #Фиксация размера окна
Config.set('graphics','width','640');   #Размер ширины
Config.set('graphics','height','480');  #Размер высоты

from kivy.uix.floatlayout import FloatLayout #Изменять размеры кнопки
from kivy.uix.scatter import Scatter

class MyApp(App):
	def build(self):

		s = Scatter()
		f1 = FloatLayout(size = (300,300))
		s.add_widget(f1)
		f1.add_widget(Button(
			text = "Это моя первая кнопка!",
			font_size = 16,
			on_press = self.btn_press,
			background_color = [1, 0, 0, 1],
			background_normal = '',
			size_hint = (.5, .25),
			pos = (0,100)));

		return s 

	def btn_press(self, instance):
		print('Конпка нажата')
		instance.text = 'Я нажата'

if __name__ == "__main__":
	MyApp().run()
