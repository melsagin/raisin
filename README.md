# Raisin Data
Bu çalışmadaki veriseti, Türkiye'de yetiştirilen iki farklı kuru üzüm çeşidinin (Keçimen ve Besni) birbirinden ayırt edilebilmesi amacıyla makine görme sistemi kullanılarak her iki çeşitten eşit sayıda olmak üzere toplam 900 adet kuru üzüm tanesi incelenmiştir. Bu görüntüler çeşitli ön işleme adımlarına tabi tutulmuş ve görüntü işleme teknikleri kullanılarak 7 adet morfolojik özellik çıkarma işlemi gerçekleştirilmiştir. 

Bu noktada ben de bu verisetini kullanarak öncelikle özellikler arasındaki ilişkiyi veri görselleştirme yöntemleriyle anlamayı daha sonra ise makine öğrenmesi algoritmalarından Logistic Regression, KNN ve SVM tercih edilerek üzüm çeşitlerini diğer özelliklere bağlı kalarak tahmin etmeyi amaçlamaktayım. Sonunda da kullanılan makine öğrenmesi algoritmalarının performanslarını değerlendirmeyi amaçlamaktayım.

![Area](https://github.com/melsagin/raisin/assets/95714510/eb50a36a-4e37-4992-a9c4-295359b0df90)


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
