# Raisin Data
Bu çalışmadaki veri seti, Türkiye'de yetiştirilen iki farklı kuru üzüm çeşidinin (Keçimen ve Besni) birbirinden ayırt edilebilmesi amacıyla makine görme sistemi kullanılarak her iki çeşitten eşit sayıda olmak üzere toplam 900 adet kuru üzüm tanesi incelenmiştir. Bu görüntüler çeşitli ön işleme adımlarına tabi tutulmuş ve görüntü işleme teknikleri kullanılarak 7 adet morfolojik özellik çıkarma işleminden geçerek aşağıdaki forma ulaşmıştır.

- 1 - Area (Alan): Üzüm sınırları içindeki piksel sayısını verir 
- 2 - MajorAxisLength (Büyük Eksen Uzunluğu): Üzüm üzerine çizilebilecek en uzun çizgi olan ana ekseni uzunluğunu - verir 
- 3 - MinorAxisLength (Küçük Eksen Uzunluğu): Üzüm üzerine çizilebilecek en kısa çizgi olan küçük ekseni uzunluğunu verir 
- 4 - Eccentricity (Eksantriklik): Aynı momentlere sahip olan elipsin eksantrikliğini ölçer 
- 5 - ConvexArea (Konveks Alan): Üzüm tarafından oluşturulan bölgenin en küçük konveks kabuğundaki piksel sayısını verir 
- 6 - Extent (Yayılım): Üzüm tarafından oluşturulan bölgenin sınırlayıcı kutudaki toplam piksellere oranını verir 
- 7 - Perimeter (Çevre): Üzüm sınırları ve etrafındaki pikseller arasındaki mesafeyi hesaplayarak çevreyi ölçer 
- 8 - Class (Sınıf): Keçimen ve Besni üzümü

Bir elips için eksantriklik, şeklin mükemmel bir daire olmaktan ne kadar sapkın olduğunu ölçen boyutsuz bir parametredir. Eksantriklik değeri 0 ile 1 arasında değişir.

- Eksantriklik 0 ise, elips mükemmel bir dairedir.
- Eksantriklik 1'e yaklaştıkça, elips daha uzun ve "düzleşmiş" hale gelir, ince bir oval şekline benzer.
- Eksantriklik tam olarak 1 ise, şekil bir paraboladır.
- Eksantriklik 1'den büyükse, şekil bir hiperbol olur.

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

## Projeinin Amacı
Veri setindeki iki çeşit kuru üzümün diğer morfolojik özelliklerden yola çıkarak doğru tahmin edilmesi.

## Problem ve Önemi
Tarım ve gıda sektöründe kuru üzüm çeşitlerini doğru bir şekilde tahmin etmek, üreticilere ve işletmelere kalite kontrol süreçlerinde yardımcı olabilir. Bu, üretim süreçlerini optimize etme, kaynakları verimli kullanma ve nihai ürün kalitesini artırma açısından kritik bir öneme sahiptir.

## Projenin Hedefleri
Bu noktada ben de bu verisetini kullanarak öncelikle özellikler arasındaki ilişkiyi veri görselleştirme yöntemleriyle anlamayı daha sonra ise makine öğrenmesi algoritmalarından Logistic Regression, KNN ve SVM tercih edilerek üzüm çeşitlerini diğer özelliklere bağlı kalarak tahmin etmeyi hedeflemekteyim. Sonunda da kullanılan makine öğrenmesi algoritmalarının performanslarını değerlendirmeyi hedefliyorum.

## Veri Temizleme
Veri temizleme aşamasında aykırı değerler yer alıyordu. Aykırı değerlerden arınmak için filtreleme yöntemi kullanılarak düzeltme yoluna girildi.

## Model Seçimi ve Sonuçlar:
Model seçim sürecinde Logistic Regresyon, K-Nearest Neighbors ve Support Vector Machine makine öğrenim modelleri değerlendirildi. Bu modellerin veri setindeki özellikleri kullanarak kuru üzüm çeşitlerini başarıyla tahmin edebildiği görüldü. Modellerin başarı oranları üzerinden yapılan testlerde yüksek doğruluk ve hassasiyet elde edildi.

# Raisin Data
In this study, a dataset consisting of a total of 900 raisin grains, 450 from each of the two different raisin varieties grown in Turkey (Keçimen and Besni), was examined using a machine vision system to distinguish between them. These images underwent various preprocessing steps and went through 7 morphological feature extraction processes using image processing techniques to achieve the following form.

- 1 - Area: Represents the number of pixels within the boundaries of the raisin.
- 2 - MajorAxisLength: Gives the length of the major axis, the longest line that can be drawn on the raisin.
- 3 - MinorAxisLength: Gives the length of the minor axis, the shortest line that can be drawn on the raisin.
- 4 - Eccentricity: Measures the eccentricity of the ellipse with the same moments.
- 5 - ConvexArea: Gives the number of pixels in the smallest convex hull of the region created by the raisin.
- 6 - Extent: Gives the ratio of the total pixels in the bounding box of the region created by the raisin.
- 7 - Perimeter: Measures the perimeter by calculating the distance between the boundaries of the raisin and surrounding pixels.
- 8 - Class: Keçimen and Besni raisin.

Eccentricity for an ellipse is a dimensionless parameter that measures how far the shape is from being a perfect circle. The eccentricity value ranges from 0 to 1.

- Eccentricity 0: The ellipse is a perfect circle.
- As Eccentricity approaches 1, the ellipse becomes longer and "flattened," resembling a thin oval shape.
- Eccentricity exactly 1: The shape is a parabola.
- If Eccentricity is greater than 1, the shape becomes a hyperbola.

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

## Project Purpose
To predict the two types of raisins in the dataset based on other morphological features.

## Problem and Importance
Accurately predicting the types of raisin varieties in the agriculture and food sector can help producers and businesses in quality control processes. This is critical for optimizing production processes, efficiently using resources, and improving the overall product quality.

## Project Goals
At this point, using this dataset, my goal is to first understand the relationship between features using data visualization methods and then predict grape varieties based on other features by using machine learning algorithms such as Logistic Regression, KNN, and SVM. Finally, I aim to evaluate the performance of the machine learning algorithms used.

## Data Cleaning
During the data cleaning stage, there were outliers. To get rid of outliers, a filtering method was used for correction.

## Model Selection and Results
In the model selection process, Logistic Regression, K-Nearest Neighbors, and Support Vector Machine machine learning models were evaluated. It was observed that these models successfully predicted grape varieties based on dataset features. Tests based on model success rates yielded high accuracy and precision.








