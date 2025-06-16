from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model classification
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
 
"""
Función de pérdida: que tan bien lo ha hecho el modelo
Binary_crossentropy: función de pérdida para problemas de clasificación binaria
Optimizador: Ajustar pesos
Pesos: lo q la red aprende

loss: Regression=MSE
	  Clasificación binaria: binary_crossentropy
	  Clasificación multiclase: categorical_crossentropy


"""
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10,verbose=0) # Verbose 0  hace q no se muestren las barras de carga
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# make class predictions with the model
predictions = (model.predict(X) > 0.5).astype(int)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))