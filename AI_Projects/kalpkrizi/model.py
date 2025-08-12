import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore


# ------------------------------
# 1. Veri Yükleme ve Ön İşleme
# ------------------------------
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)

    label_encoders = {}
    categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df.drop('HeartDisease', axis=1)
    y = df['HeartDisease']

    return X, y, label_encoders

# ------------------------------
# 2. Eğitim/Test Bölme ve SMOTE
# ------------------------------
def split_and_balance(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    smote = SMOTE(random_state=42)
    X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
    return X_train_smote, X_test, y_train_smote, y_test

# ------------------------------
# 3. Ölçeklendirme
# ------------------------------
def scale_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

# ------------------------------
# 4. Modelleri Eğitme
# ------------------------------
def build_ann(input_dim):
    model = Sequential([
        Dense(16, input_dim=input_dim, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer=Adam(0.001), metrics=['accuracy'])
    return model

def train_models(X_train_scaled, y_train, X_test_scaled, y_test):
    results = {}

    # ANN
    ann_model = build_ann(X_train_scaled.shape[1])
    ann_model.fit(X_train_scaled, y_train, epochs=50, verbose=0, validation_data=(X_test_scaled, y_test))
    _, ann_acc = ann_model.evaluate(X_test_scaled, y_test, verbose=0)
    results["Yapay Sinir Ağı"] = ann_acc * 100

    # Random Forest
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    results["Random Forest"] = accuracy_score(y_test, rf_model.predict(X_test_scaled)) * 100

    # Decision Tree
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train_scaled, y_train)
    results["Karar Ağaçları"] = accuracy_score(y_test, dt_model.predict(X_test_scaled)) * 100

    # Logistic Regression
    lr_model = LogisticRegression(random_state=42)
    lr_model.fit(X_train_scaled, y_train)
    results["Lojistik Regresyon"] = accuracy_score(y_test, lr_model.predict(X_test_scaled)) * 100

    return results, ann_model

# ------------------------------
# 5. Kullanıcıdan Veri Alıp Tahmin
# ------------------------------
def predict_user_input(model, scaler, label_encoders):
    try:
        user_data = {
            'Age': float(input('Yaşınızı giriniz: ')),
            'Sex': label_encoders['Sex'].transform([input('Cinsiyetiniz (M/F): ').strip()])[0],
            'ChestPainType': label_encoders['ChestPainType'].transform([input('Göğüs Ağrısı Tipi (ATA/NAP/ASY/TA): ').strip()])[0],
            'RestingBP': float(input('Dinlenme Kan Basıncınızı giriniz: ')),
            'Cholesterol': float(input('Kolesterol değeriniz: ')),
            'FastingBS': 0,
            'RestingECG': 0,
            'MaxHR': 150,
            'ExerciseAngina': 0,
            'Oldpeak': 0.0,
            'ST_Slope': 1
        }
    except ValueError:
        print("❌ Geçersiz giriş yaptınız. Lütfen sayısal değerleri doğru girin.")
        return

    user_df = pd.DataFrame([user_data])
    user_scaled = scaler.transform(user_df)
    prediction = model.predict(user_scaled)
    print(f"💓 Tahmin sonucu: Kalp hastalığı risk oranınız {prediction[0][0] * 100:.2f}%")

# ------------------------------
# 6. Ana Çalışma
# ------------------------------
if __name__ == "__main__":
    X, y, label_encoders = load_and_preprocess_data("heart.csv")
    X_train, X_test, y_train, y_test = split_and_balance(X, y)
    X_train_scaled, X_test_scaled, scaler = scale_data(X_train, X_test)

    results, ann_model = train_models(X_train_scaled, y_train, X_test_scaled, y_test)

    print("\n📊 Model Doğruluk Oranları:")
    for model_name, acc in results.items():
        print(f"{model_name}: {acc:.2f}%")

    while True:
        predict_user_input(ann_model, scaler, label_encoders)
        if input("Başka tahmin yapmak ister misiniz? (E/H): ").lower() != "e":
            break
