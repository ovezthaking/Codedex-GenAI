from translate import Translator

translator = Translator(to_lang='es')

text = 'Hello, I\'m learning new things like machine learning and artificial intelligence. And you?'

translation = translator.translate(text)

print(f'Translated text: {translation}')
