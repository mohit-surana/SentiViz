import csv
import sys

from keras.models import Sequential
from keras.layers import *
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

from gensim.models import Word2Vec

import numpy as np

from preprocess import clean_tweet

class BinarizedSentimentAnalyzer:
	def __init__(self, input_dim=32, hidden_dim=64, dropout=0.3):
		np.random.seed(7)

		self.model = Sequential()
		self.model.add(recurrent.LSTM(input_shape=(None, input_dim), output_dim=hidden_dim, init="he_normal", dropout_W=dropout, dropout_U=dropout))
		self.model.add(Activation('tanh'))
		self.model.add(Dense(2, init="lecun_uniform", activation='softmax'))
		self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	def train(self, X_train, Y_train, X_val, Y_val, epochs=5, batch_size=32):
		print(self.model.summary())
		self.model.fit(X_train, Y_train, nb_epoch=epochs, shuffle=True, batch_size=batch_size, validation_data=(X_val, Y_val))

	def test(self, X_test, Y_test):
		return self.model.evaluate(X_test, Y_test, verbose=0)[1]

	def predict(self, inputs):
		tweets = np.array([sent_to_w2v(clean_tweet(t)) for t in inputs])
		tweets = sequence.pad_sequences(tweets, maxlen=20)
		# tweets = tweets.reshape(1, tweets.shape[0], tweets.shape[1])
		predictions = self.model.predict(tweets, verbose=0)
		# print predictions
		return {0: [inputs[i] for i in range(len(inputs)) if np.argmax(predictions[i]) == 0 ], 1: [inputs[i] for i in range(len(inputs))  if np.argmax(predictions[i]) == 1]}
		
	def save(self):
		self.model.save('lstm_model.h5')


__model = None
def sent_to_w2v(sentence):
	global __model

	if not __model:
		__model = Word2Vec.load('senti_viz/w2v.pkl')
		print 'Loaded w2v.pkl'

	word_list = sentence.split(" ")
	w2v_list = []
	for word in word_list:
		try:
			w2v_list.append(__model[word])
		except:
			pass

	return np.array(w2v_list)

if __name__ == "__main__":
	X_data = []
	Y_data = []

	train_size = 20

	sanitizer = BinarizedSentimentAnalyzer()

	with open('CleanData.csv', 'rb') as csvfile:
	    reader = csv.reader(csvfile)
	    for i, row in enumerate(reader):
			if i == train_size:
				break

			print i
			X_data.append(sent_to_w2v(row[0]))
			v = np.array([0, 0])
			v[row[1]] = 1
			Y_data.append(v)   
   

	X_train = np.array(X_data[: int(len(X_data) * 0.75) ])
	Y_train = np.array(Y_data[: int(len(X_data) * 0.75) ])

	X_val = np.array(X_data[int(len(X_data) * 0.75) : int(len(X_data) * 0.9)])
	Y_val = np.array(Y_data[int(len(X_data) * 0.75) : int(len(X_data) * 0.9)])

	X_test = np.array(X_data[int(len(X_data) * 0.9) :])
	Y_test = np.array(Y_data[int(len(X_data) * 0.9) :])

	X_train = sequence.pad_sequences(X_train, maxlen=20)
	X_val = sequence.pad_sequences(X_val, maxlen=20)
	X_test = sequence.pad_sequences(X_test, maxlen=20)

	sanitizer.train(X_train, Y_train, X_val, Y_val)
	print str(sanitizer.test(X_test, Y_test) * 100) + '%'

	sanitizer.save()