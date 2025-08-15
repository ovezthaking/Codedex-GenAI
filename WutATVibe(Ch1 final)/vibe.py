from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


reviews = [
    'I liked it just as much as the first one',
    'High production values but the story feels cliched, pace is slow to glacial, characters are hard to get invested in and the dialogue is stilted. It takes some effort to make a story about being chased by criminal masterminds so boring...',
    'It\'s such a shame, a brilliant cast, lovely setting, obviously a huge budget... yet the story was as if a bunch of stoned teenagers suddenly said to each other, \'hey, got a great idea for a tv show\' and came up with the most ridiculous and inane script ever written. Sorry, but with all of the hype and trailers, I was hoping for so much more. Please don\'t make a second series, and spend the money on something better.',
    'Lighthearted and funny. Waiting for another season. Good acting, they’ve great chemistry.',
    'Even better in this second season!',
    'This movie was fantastic! A must-watch.',
    'I didn\'t enjoy this movie at all.',
    'Amazing storyline and great acting!',
    'The plot was dull and predictable.',
    'Loved the cinematography! Highly recommended.'
]

labels = ['positive', 'negative',
          'negative', 'positive', 'positive',
          'positive', 'negative', 'positive',
          'negative', 'positive'
          ]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2,
                                                    random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)

if accuracy > 0.8:
    print('Good vibes')
else:
    print("Needs more work!")
