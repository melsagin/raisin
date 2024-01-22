# Raisin Veri Seti Hakkında
Bu çalışmadaki veri seti, Türkiye'de yetiştirilen iki farklı kuru üzüm çeşidinin (Keçimen ve Besni) birbirinden ayırt edilebilmesi amacıyla makine görme sistemi kullanılarak her iki çeşitten eşit sayıda olmak üzere toplam 900 adet kuru üzüm tanesi incelenmiştir. Bu görüntüler çeşitli ön işleme adımlarına tabi tutulmuş ve görüntü işleme teknikleri kullanılarak 7 adet morfolojik özellik çıkarma işleminden geçerek aşağıdaki forma ulaşmıştır.

1 - Area (Alan): Üzüm sınırları içindeki piksel sayısını verir
2 - MajorAxisLength (Büyük Eksen Uzunluğu): Üzüm üzerine çizilebilecek en uzun çizgi olan ana ekseni uzunluğunu verir
3 - MinorAxisLength (Küçük Eksen Uzunluğu): Üzüm üzerine çizilebilecek en kısa çizgi olan küçük ekseni uzunluğunu verir
4 - Eccentricity (Eksantriklik): Aynı momentlere sahip olan elipsin eksantrikliğini ölçer
5 - ConvexArea (Konveks Alan): Üzüm tarafından oluşturulan bölgenin en küçük konveks kabuğundaki piksel sayısını verir
6 - Extent (Yayılım): Üzüm tarafından oluşturulan bölgenin sınırlayıcı kutudaki toplam piksellere oranını verir
7 - Perimeter (Çevre): Üzüm sınırları ve etrafındaki pikseller arasındaki mesafeyi hesaplayarak çevreyi ölçer
8 - Class (Sınıf): Keçimen ve Besni üzümü

Bir elips için eksantriklik, şeklin mükemmel bir daire olmaktan ne kadar sapkın olduğunu ölçen boyutsuz bir parametredir. Eksantriklik değeri 0 ile 1 arasında değişir.

- Eksantriklik 0 ise, elips mükemmel bir dairedir.
- Eksantriklik 1'e yaklaştıkça, elips daha uzun ve "düzleşmiş" hale gelir, ince bir oval şekline benzer.
- Eksantriklik tam olarak 1 ise, şekil bir paraboladır. 
- Eksantriklik 1'den büyükse, şekil bir hiperbol olur.

# Projenin Amacı
Veri setindeki iki çeşit kuru üzümün diğer morfolojik özelliklerden yola çıkarak doğru tahmin edilmesi
Bu noktada ben de bu verisetini kullanarak öncelikle özellikler arasındaki ilişkiyi veri görselleştirme yöntemleriyle anlamayı daha sonra ise makine öğrenmesi algoritmalarından Logistic Regression, KNN ve SVM tercih edilerek üzüm çeşitlerini diğer özelliklere bağlı kalarak tahmin etmeyi amaçlamaktayım. Sonunda da kullanılan makine öğrenmesi algoritmalarının performanslarını değerlendirmeyi amaçlamaktayım.

# Problem ve Önemi
Tarım ve gıda sektöründe kuru üzüm çeşitlerini doğru bir şekilde tahmin etmek, üreticilere ve işletmelere kalite kontrol süreçlerinde yardımcı olabilir. Bu, üretim süreçlerini optimize etme, kaynakları verimli kullanma ve nihai ürün kalitesini artırma açısından kritik bir öneme sahiptir.

# Ön Analiz Bulguları
Kuru üzüm çeşitlerinin belirli özellikler üzerinden ayrıştırılabileceğini ve bu özelliklerin tahmin modeline entegre edilebileceğini görüldü.

# Veri Temizleme
Veri temizleme aşamasında karşılaşılan zorluklar arasında aykırı değerler yer alıyordu. Bu zorluğu aşmak için aykırı değerleri filtreleme yöntemi kullanılarak düzeltme yoluna girildi.

# Model Seçimi ve Sonuçlar:
Model seçim sürecinde, çeşitli makine öğrenimi modelleri değerlendirildi. Bu modeller, veri setindeki özellikleri kullanarak kuru üzüm çeşitlerini başarıyla tahmin edebiliyor. Modellerin başarı oranları üzerinden yapılan testlerde, yüksek doğruluk ve hassasiyet elde edildi.

## Kurulum
- Depoyu klonlayın:
    - `git clone https://github.com/melsagin/raisin.git`

## Gereksinimler
Scripti çalıştırmadan önce, requirements.txt içerisindeki kütüphaneleri içe aktarmayı unutmayınız.

## Dosyaların İçeriği
- analysis.ipynb
    - İçe aktarılan fonksiyonlar çağrılarak çalışma prensibi analiz edilir
- method.py 
    - Fonksiyonları içerir

# Raisin Data
In this study, a dataset comprising equal numbers of two different types of raisins grown in Turkey (Keçimen and Besni) was examined. The aim was to distinguish between the two types using a machine vision system, and a total of 900 raisins, 450 from each variety, were analyzed. These images underwent various preprocessing steps, and 7 morphological features were extracted using image processing techniques.

At this point, my goal is to first understand the relationship between the features through data visualization methods using this dataset. Subsequently, I aim to predict the raisin varieties while considering other features, using machine learning algorithms such as Logistic Regression, KNN, and SVM. Finally, I intend to evaluate the performance of the machine learning algorithms used.

## Installation
- Clone the repository:
    - `git clone https://github.com/melsagin/raisin.git`

## Requirements
Before running the script, make sure to import the libraries in the requirements.txt file.

## File Contents
- analysis.ipynb
    - Analyzes the working principle by calling the imported functions
- api_methods.py
    - Contains functions