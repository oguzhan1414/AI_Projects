import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = {
    "Yil": [2010, 2015, 2018, 2020, 2012, 2016, 2019],
    "Km": [150000, 90000, 60000, 30000, 130000, 80000, 40000],
    "Motor_Hacmi": [1600, 1400, 1200, 1600, 1800, 1600, 1500],
    "Fiyat": [150000, 200000, 250000, 320000, 170000, 220000, 280000]
}

df = pd.DataFrame(data)

X= df[["Yil","Km","Motor_Hacmi"]] #input
y = df["Fiyat"] #output
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

y_predict = model.predict(X_test)
mse = mean_squared_error(y_test,y_predict)
rmse = np.sqrt(mse)

yil_input = int(input("Yılı giriniz"))
km_input = int(input("Km Giriniz"))
motor_hacmi_input = int(input("Motor Hacmi giriniz"))

tahmin_etme = model.predict([[yil_input,km_input,motor_hacmi_input]])
print(f"Tahmini Fiyat: {tahmin_etme[0]:.0f}")