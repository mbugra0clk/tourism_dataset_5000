import pandas as pd

df = pd.read_csv('C:\ML/tourism_dataset_5000/tourism_dataset_5000.csv')

# İlgili kolonları inceleyelim
columns_of_interest = ["Interests", "Sites Visited", "Tourist Rating"]
df[columns_of_interest].head(10)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Sütun isimlerini küçük harfe çevir (Eğer fark olursa)
df.columns = df.columns.str.strip().str.lower()

# ✅ Liste formatındaki verileri string hale getirme fonksiyonu
def list_to_string(lst):
    if isinstance(lst, str):
        try:
            lst = ast.literal_eval(lst)  # String içindeki listeyi doğru formata çevir
        except:
            return lst  # Eğer hata olursa olduğu gibi bırak
    if isinstance(lst, list):
        return " ".join(lst)  # Liste elemanlarını tek string haline getir
    return str(lst)

# "interests" ve "sites visited" kolonlarını birleştirerek içerik oluştur
df["features"] = df["interests"].apply(list_to_string) + " " + df["sites visited"].apply(list_to_string)

# TF-IDF vektörleştirme
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["features"])

# Cosine Similarity hesaplama
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Kullanıcı için öneri yapan fonksiyon
def get_recommendations(user_id, df, cosine_sim):
    if user_id not in df["tourist id"].values:
        return f"Hata: Tourist ID {user_id} bulunamadı."

    # Kullanıcının indexini bul
    idx = df.index[df["tourist id"] == user_id].tolist()[0]

    # Kullanıcıya en benzeyen diğer turistleri al
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Kullanıcının kendisini listeden çıkar
    sim_scores = sim_scores[1:4]  # İlk 3 benzer kişiyi al

    # Öneri yapılacak kişilerin indekslerini al
    user_indices = [i[0] for i in sim_scores]

    # Öneri yapılacak ziyaret noktalarını al
    recommended_places = []
    for i in user_indices:
        places = ast.literal_eval(df.iloc[i]["sites visited"]) if isinstance(df.iloc[i]["sites visited"], str) else df.iloc[i]["sites visited"]
        recommended_places.extend(places)

    return list(set(recommended_places))  # Tekrar eden yerleri kaldır

# Kullanıcıdan Tourist ID girmesini iste
user_input = input("Lütfen Tourist ID girin: ")
try:
    user_id = int(user_input)  # Sayıya çevir
    recommended_sites = get_recommendations(user_id, df, cosine_sim)
    print(f"📍 Tourist ID {user_id} için önerilen yerler: {recommended_sites}")
except ValueError:
    print("❌ Hata: Lütfen geçerli bir sayı girin.")
