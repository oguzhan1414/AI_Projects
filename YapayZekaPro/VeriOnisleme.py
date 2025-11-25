import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
data = {
    'Yaş': [25, 30, np.nan, 35, 40, 45, 50, 22, 900], # 1 eksik veri, 1 aykırı değer (900)
    'Maaş': [50000, 55000, 60000, 65000, 150000, 75000, 80000, 48000, np.nan], # 1 eksik veri, 1 aykırı değer (150000)
    'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'İstanbul', 'Ankara', 'Bursa', 'İzmir', 'İstanbul', 'Ankara'],
    'Memnuniyet': ['Orta', 'Yüksek', 'Düşük', 'Yüksek', 'Orta', 'Düşük', 'Yüksek', 'Orta', 'Orta'] # Sıralı (Ordinal) kategori
}

df = pd.DataFrame(data)

print(df)

print("Eksik Veri Tespiti")
print(df.isnull().sum())

"""  Burda eksik verilerimizi siliyoruz ama bu yaklaşım yerine
df_silinmis = df.dropna()
print(df_silinmis)
"""

df_temiz = df.copy()
yas_median = df_temiz["Yaş"].median()
df_temiz["Yaş"] = df_temiz["Yaş"].fillna(yas_median)
print(df_temiz)

maas_median = df_temiz["Maaş"].median()
df_temiz["Maaş"] = df_temiz["Maaş"].fillna(yas_median)

df_donusum = pd.get_dummies(df_temiz,columns=["Şehir"])
print("Şehir için One-Hot ENCODİNG")
print(df_donusum.head())

memnuniyet_map = {
    'Düşük' : 0,
    'Orta' : 1,
    "Yüksek" : 2
}
df_donusum["Memnuniyet"] = df_donusum["Memnuniyet"].map(memnuniyet_map)
print(df_donusum)

####STANDART YAPMA
numeric_cols = ["Yaş","Maaş"]  ##diğer sütünlar zaten 0-1 formatında
scaler = StandardScaler()

df_son_hali = df_donusum.copy()
df_son_hali[numeric_cols] = scaler.fit(df_son_hali[numeric_cols])
print(df_son_hali)