import numpy as np
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense  # type: ignore

#giriş verileri XOR problemei olarak al
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

#basit model
model = Sequential()
model.add(Dense(4,input_dim =2,activation='relu')) #relu doğru veya yanlış olarak filtre 2 li veri setinde input_dim o anlamda
model.add(Dense(1,activation='sigmoid')) #1çıkışımız olacak sigmoid de 0 - 1 arasında atıyor dış dünyaya 0.50 den küçükse 0 büyükse 1

#modeli derleme
model.compile(loss='binary_crossentropy',optimizer = 'adam',metrics=['accuracy']) #hatalar küçük küçük parçalara böler  adam ise parçaları düzeltir

#modeli eğitme
model.fit(X,y,epochs=100,verbose=1) #100 kere çalıştır ve her çalıştırmada verbose = 1 sonuç verir

tahminleme = model.predict(X)
print(f"tahminler: {tahminleme}")
