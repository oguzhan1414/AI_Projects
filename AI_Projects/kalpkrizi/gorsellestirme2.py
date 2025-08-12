import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("heart.csv")


#histogram analizi
df.hist(figsize=(18,12),bins=20,edgecolor="black")
plt.suptitle("Veri Dağılımı")
#plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=df,x="Age",y="Cholesterol",hue="HeartDisease")
plt.title("Yaş ve Kolestrol arasındaki ilişki")
#plt.show()

label_encode = LabelEncoder()
df["Sex"] = label_encode.fit_transform(df["Sex"])
df["ChestPainType"] = label_encode.fit_transform(df["ChestPainType"])
df["RestingECG"] = label_encode.fit_transform(df["RestingECG"])
df["ExerciseAngina"] = label_encode.fit_transform(df["ExerciseAngina"])
df["ST_Slope"] = label_encode.fit_transform(df["ST_Slope"])

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm",fmt=".2f")
#plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x="HeartDisease",data=df)
plt.title("Kalp Hastalığına yakalanma oranı")
plt.show()
