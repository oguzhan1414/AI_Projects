import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
##veriyi yükle

df = pd.read_csv("heart.csv")

###print(df.info())
##print(df.isnull().sum())

#kategorik sütunlar
categorical_colums = ["ChestPainType","Sex","RestingECG","ExerciseAngina","ST_Slope"]
#LABEL İLE BU SÜTÜNLARI SAYISAL HALE GETİRME

le = LabelEncoder()
for colum in categorical_colums:
    df[colum] = le.fit_transform(df[colum])

##verileri standart hale getirme
numeric_columns = ["Age","RestingBP","Cholesterol","FastingBS","MaxHR","Oldpeak"]
scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

df.to_csv("heart_duzenlenmis.csv",index=False)
