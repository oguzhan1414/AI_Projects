import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer #kelimeleri kök formuna indirir running run olur misal
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

nltk.download("stopwords")
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

df = pd.read_csv("spam.csv",encoding="latin-1")[["v1","v2"]] #iki sütunu seçtik
df.columns = ["label","message"]
df["label"] = df["label"].map({"ham":0,"spam":1}) ##burda normalizasyon yapmış olduk
print(df.head())

def preprocess_text(text):
    text = re.sub(r"\W", " ", text) #remove special characters
    text = text.lower() #Convert to lowercase
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

df["cleaned_message"] = df["message"].apply(preprocess_text) #önişleme yaptık
print(df.head())

vectorizer = TfidfVectorizer(max_features=3000) #vectorizer ile metni sayısallaştırdık
X = vectorizer.fit_transform(df["cleaned_message"])
y = df["label"]

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test) #xtest için modelimizi doğruluğu test etcez
print(f"Accuracy: {accuracy_score(y_test,y_pred) * 100:.2f}%")
print(classification_report(y_test,y_pred))

def predict_email(email_text):
    procces_text = preprocess_text(email_text)
    vectroized_text = vectorizer.transform([procces_text])
    prediction = model.predict(vectroized_text)
    return "Spam" if prediction[0] == 1 else "Not Spam"


email = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."
print(f"Email : {email} \nPrediction: {predict_email(email)}")