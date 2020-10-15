import pyttsx3

def speak(text):
	"""
		Функция для воспроизведения текста

		Agrs:
			text(str): строка для воспроизведения
	"""
	engine = pyttsx3.init()
	engine.say(str(text))
	engine.runAndWait()


def main():
	speak(text="Test")
	speak(text="Тест")


if __name__ == '__main__':
	main()