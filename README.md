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
- data (raisin.csv)
    - Veri setinin bulunduğu dosyadır

## Projeinin Amacı
Veri setindeki iki çeşit kuru üzümün diğer morfolojik özelliklerden yola çıkarak doğru tahmin edilmesi.

## Bu verisetini neden seçtim?
Tarım sektörünün çiftçilerin geçimini sağlamakta yaşadığı zorluklardan dolayı sektörün durma aşamasında olduğunu biliyoruz. Gıda sektöründe ise kendi ürünlerimizi üretememek, dışa bağımlılığımızı artırıyor. Bu bağlamda, projemde kullanılan makine öğrenmesi algoritmaları sayesinde, tarım ve gıda sektöründeki manuel ve zaman alıcı işlemlerin otomatize edilebileceğini göstermeye çalıştım. Buradaki hedefim de Türkiye’de gıda ve tarım sektöründeki çalışmaların azalmasına dair dikkat çekmekle birlikte, veri bilimi ve makine öğrenmesiyle bu sektörlere nasıl bir katkı sağlayabileceğini göstermeyi amaçladım.

## Projenin Hedefleri
Bu noktada ben de bu verisetini kullanarak öncelikle özellikler arasındaki ilişkiyi veri görselleştirme yöntemleriyle anlamayı daha sonra ise makine öğrenmesi algoritmalarından Logistic Regression, KNN ve SVM tercih edilerek üzüm çeşitlerini diğer özelliklere bağlı kalarak tahmin etmeyi hedeflemekteyim. Sonunda da kullanılan makine öğrenmesi algoritmalarının performanslarını değerlendirmeyi hedefliyorum.

## Ön Bulgular
Ön Analiz sonucunda feauture’lar arasında logaritmik bir ilişki olduğunu ve sınıflandırma modellerine uygun olduğu görüldü. 
- Besni değer olarak daha fazla yayılım gösterirken Keçimen daha dar bir yayılım göstermiştir.
- Besni ve Keçimen türünün sayıları eşittir.
- Feauture’ler arasında yüksek korelasyon tespit edilmiştir.

## Veri Temizleme
Veri temizleme aşamasında eksik veri yoktu ancak daha önce görselleştirme kısmındaki box plot örneğinden aykırı değerler olabileceğine dair bir öngörü oluştu.
Bu noktada aykırı değerleri çıkarabilmek için IQR (Çeyrekler Arası Aralık) yöntemi kullanılmıştır. Bu yöntem
- İlk çeyrek (Q1) ve üçüncü çeyrek (Q3) bulunur
- IQR hesaplanır = Q3 – Q1 
- Üst sınır hesaplanır = Q3 + (1,5 * IQR) 
- Alt sınır hesaplanır = Q1 – (1,5 * IQR) 
- Sınırların dışında kalan tüm değerler, satır bazında iki taneden fazlasysa aykırı değer olarak kabul edilir.
aşamalarını kapsayan bir yöntemdir. 

Bu yöntem sonucunda aykırı değerlere ağırlıklı olarak Besni türünde rastlanmaktadır (Besni [33/35], Keçimen[2/35]) bu da modelimin tahmin aşamasında aslında işe yarayan niteliğe sahip olabileceğini göstermektedir bu nedenle aykırı değerler silinmeden modellerin oluşturulup test edilmesine karar verilmiştir. Ancak modelin değerlendirilmesi kısmında aykırı değerler ile nasıl bir sonuç verileceğine dair de bir kısım bulunmaktadır.

## Model Seçimi ve Sonuçlar:
Model seçim sürecinde değişkenler arasındaki logaritmik ilişki ve tahmin edilen hedef değişkenin binary (0 ve 1) olmasından dolayı Logistic Regresyon, veri noktalarının birbirine yakın bir kümelenme göstermiş olmaları nedeniyle K-Nearest Neighbor ve çoklu bağlantı sorunundan etkilenmemesinin yanı sra veriyi bir hiperdüzlem kurarak yüksek marj ile iki sınıfa bölebilmesi nedeniyle Support Vector Machine modelleri uygulandı. 

Modeller oluşturulurken model performansının daha gerçekçi sonuçlar verebilmesi amacıyla Cross Validation yapıldı, iyi performanslar vermesi amacıyla da hiperparemetre seçimi noktasında GridSearchCV kullanılmıştır. Tüm modellerin accuracy, precision, recall ve f1 skorlarına bakılmıştır. Bunun dışında ayrıca LR için Log Loss, KNN için MSE ve RMSE’ye  SVM için ise ROC-AUC eğrisine bakılmıştır. Buradan çıkan sonuçların 0 ile 1 arasında 0’a yakın değerler olması modelimizin hata oranlarının da düşük olduğunu göstermektedir.

Accuracy, precision, recall ve f1 skorlarıyla bir analiz yapılmış ve modellerin en yüksek başarı oranları üzerinden yapılan testlerde random_state= 39 iken KNN %88 ile en yüksek performansı verirken, SVM %87 ile LR ise %86 ile diğer modelleri takip etmiştir. 
Son olarak aykırı değerler çıkarılarak yapılan analiz sonucunda ise %90 ile en yüksek performansı KNN modeli gösterirken LR ve SVM modellerinin %86 ile aynı performans sonucunu verdiği gözlemlenmiştir. 

Bu performans verilerinden yola çıkarak kullanılan modellerin biribirine yakın performans oranları gösterdiği ve kuru üzüm çeşitlerini başarıyla tahmin edebildiği görüldü.

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
- data (raisin.csv)
    - File which contain dataset

## Project Purpose
To predict the two types of raisins in the dataset based on other morphological features.

## Why did I choose this dataset?
We are aware that the agricultural sector is in a stagnant state due to the difficulties farmers face in making a living. In the food sector, the inability to produce our own products increases our dependence on imports. In this context, through the machine learning algorithms used in my project, I aimed to demonstrate that manual and time-consuming processes in the agriculture and food sectors can be automated. My goal here is to draw attention to the decrease in activities in the food and agriculture sector in Turkey and to show how data science and machine learning can contribute to these sectors.

## Project Goals
At this point, by using this dataset, my primary goal is to first understand the relationship between features through data visualization methods. Then, I aim to predict grape varieties based on other features using machine learning algorithms such as Logistic Regression, KNN, and SVM. Finally, I aim to evaluate the performance of the machine learning algorithms used.

## Preliminary Findings
As a result of preliminary analysis, it was observed that there is a logarithmic relationship between the features and that it is suitable for classification models.

- Besni shows more dispersion as a value, while Keçimen shows a narrower dispersion.
- The numbers of Besni and Keçimen types are equal.
- High correlation between features was detected.

## Data Cleaning
There was no missing data in the data cleaning stage, but there was a prediction that there might be outliers based on the box plot example in the visualization part.
To remove outliers, the IQR (Interquartile Range) method was used. This method involves the following steps:

- Find the first quartile (Q1) and the third quartile (Q3).
- Calculate IQR = Q3 - Q1.
- Calculate the upper limit = Q3 + (1.5 * IQR).
- Calculate the lower limit = Q1 - (1.5 * IQR).
- All values outside the limits are considered outliers if there are more than two on a row.

As a result of this method, it was mainly encountered with outliers in the Besni type (Besni [33/35], Keçimen[2/35]). This indicates that outliers may actually have a meaningful quality in the prediction stage of the model. Therefore, it was decided to create and test models without deleting outliers. However, there is also a part about how the model will perform with outliers in the evaluation stage of the model.

## Model Selection and Results:
During the model selection process, Logistic Regression was applied due to the logarithmic relationship between variables and the binary nature (0 and 1) of the predicted target variable. K-Nearest Neighbors was chosen because the data points showed a close clustering, and Support Vector Machine models were applied because they can create a hyperplane to divide the data into two classes with a high margin, unaffected by multicollinearity.

To obtain more realistic results in terms of model performance during model creation, Cross-Validation was performed, and GridSearchCV was used for hyperparameter selection to achieve good performance. All models were evaluated based on accuracy, precision, recall, and f1 scores. In addition, Log Loss for LR, MSE and RMSE for KNN, and ROC-AUC curve for SVM were considered. The results, which are close to 0 between 0 and 1, indicate that the error rates of our model are low.

An analysis was conducted with accuracy, precision, recall, and f1 scores, and in tests based on the highest success rates, KNN provided the highest performance with 88%, while SVM with 87% and LR with 86% followed the other models. Finally, in the analysis conducted by removing outliers, it was observed that the KNN model showed the highest performance with 90%, while LR and SVM models gave the same performance result with 86%.

Based on these performance results, it was observed that the models used showed similar performance ratios and successfully predicted grape varieties.
