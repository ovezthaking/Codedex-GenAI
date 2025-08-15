from textblob import TextBlob


text = 'I love progamming and machine learnig.'

blob = TextBlob(text)

corrected_text = blob.correct()

print(f'Original text: {text}\nCorrected text: {corrected_text}')