# 🌍 Turistler İçin İçerik Tabanlı Öneri Sistemi

Bu proje, turistlerin **ilgi alanlarını** ve **ziyaret ettikleri yerleri** kullanarak, onlara benzer diğer turistlerin gezdiği noktaları öneren bir sistem geliştirmeyi amaçlamaktadır.

## 🔍 Kullanılan Veri
Bu sistem **turistlerin gezi alışkanlıklarını** temel alarak içerik tabanlı bir filtreleme yapmaktadır. Kullanılan temel veri seti şu kolonlardan oluşmaktadır:

- **Tourist ID**: Turisti benzersiz olarak tanımlayan ID
- **Interests**: Turistin ilgi alanları (müzeler, doğa, alışveriş vb.)
- **Sites Visited**: Turistin daha önce ziyaret ettiği turistik noktalar

## 🛠 Kullanılan Yöntemler
Bu sistem, **TF-IDF** ve **Cosine Similarity** yöntemlerini kullanarak turistler arasındaki benzerliği hesaplar ve buna göre öneriler sunar.

1. **Veri İşleme:** "Interests" ve "Sites Visited" kolonları birleştirilerek her turist için bir metin profili oluşturulur.
2. **TF-IDF Vektörleştirme:** Metinler, sayısal vektörlere çevrilerek anlamlı hale getirilir.
3. **Cosine Similarity:** Turistler arasındaki benzerlik hesaplanır.
4. **Öneri Yapma:** Kullanıcının seçtiği turist ID'sine en benzer diğer turistlerin gezdiği yerler listelenir.

## ✨ Nasıl Kullanılır?
Proje **Google Colab** veya **yerel ortamda** çalıştırılabilir. Kullanmak için:

1. Gerekli kütüphaneleri yükleyin:
   ```sh
   pip install pandas scikit-learn
   ```
2. Proje dosyasını çalıştırın.
3. Kullanıcıdan **Tourist ID** girmesi istenir ve sistem, en benzer turistlerin ziyaret ettiği yerleri listeler.

## 🔎 Öğrendiklerimiz
- **TF-IDF ve Cosine Similarity** kullanarak metin verisi ile benzerlik hesaplama
- **Veri düzenleme ve ön işleme teknikleri** (Listeyi string'e çevirme, eksik veriyi düzenleme)
- **Kullanıcıdan input alarak dinamik öneri yapma**

## 🌟 Gelecekte Neler Yapılabilir?
- **Makine öğrenmesi modelleri** eklenerek daha gelişmiş öneri sistemleri uygulanabilir.
- **Kullanıcı geribildirim mekanizması** ile sistemin doğruluğu artırılabilir.
- **Gerçek zamanlı veri kullanılarak** dinamik bir sistem oluşturulabilir.

---

# 🌍 Content-Based Recommendation System for Tourists

This project aims to develop a recommendation system that suggests **places to visit** for tourists based on their **interests** and **previously visited sites**.

## 🔍 Dataset
This system uses a **content-based filtering** approach, utilizing the following columns from the dataset:

- **Tourist ID**: Unique identifier for each tourist
- **Interests**: Tourist's interests (e.g., museums, nature, shopping)
- **Sites Visited**: Places the tourist has previously visited

## 🛠 Methods Used
The system uses **TF-IDF** and **Cosine Similarity** to compute the similarity between tourists and provide recommendations.

1. **Data Processing:** "Interests" and "Sites Visited" columns are merged into a single text profile.
2. **TF-IDF Vectorization:** Converts text into numerical vectors.
3. **Cosine Similarity Calculation:** Measures similarity between tourists.
4. **Recommendation Generation:** Finds similar tourists and recommends places they have visited.

## ✨ How to Use?
The project can be run on **Google Colab** or in a local environment.

1. Install the required libraries:
   ```sh
   pip install pandas scikit-learn
   ```
2. Run the project script.
3. Enter a **Tourist ID** when prompted, and the system will suggest places visited by similar tourists.

## 🔎 Key Learnings
- Using **TF-IDF and Cosine Similarity** to compute text-based similarity
- **Data preprocessing techniques** (string conversion, handling missing data)
- **Building a dynamic recommendation system** based on user input

## 🌟 Future Improvements
- Implementing **machine learning models** for enhanced recommendations.
- Adding **user feedback mechanisms** to improve recommendation accuracy.
- Using **real-time data** for dynamic recommendations.
