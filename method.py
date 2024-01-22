from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

def evaluation_metric(model, X_train, y_train, X_test, y_test):
    y_train_pred = model.predict(X_train)
    y_pred = model.predict(X_test)
    print("Train")
    print(confusion_matrix(y_train, y_train_pred))
    print(classification_report(y_train, y_train_pred))
    print()
    print("Test")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

def standardize_features(X):
    """
    Verilen bağımsız değişkenleri standartlaştırır.
    Parameters:
        X (pd.DataFrame): Standartlaştırılacak bağımsız değişkenlerin bulunduğu DataFrame. 
    Returns:
        pd.DataFrame: Standartlaştırılmış bağımsız değişkenlerin DataFrame'i.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_standardized = pd.DataFrame(X_scaled, columns=X.columns)
    return X_standardized

def encode_class(df, class_column="Class"):
    """
    Verilen DataFrame'deki "Class" kolonunu Label Encoding işlemine tabi tutar.
    Parameters:
        df (pd.DataFrame): "Class" kolonu içeren DataFrame.
        class_column (str): Label Encoding işlemi yapılacak kolon adı.
    Returns:
        pd.DataFrame: Label Encoding işlemi yapılmış DataFrame.
    """
    le = LabelEncoder()
    encoded_class = le.fit_transform(df[class_column])
    df_copy = df.copy()
    df_copy.drop(class_column, axis=1, inplace=True)
    df_copy[class_column] = encoded_class
    return df_copy

def find_best_k(X_train, y_train, max_k=20):
    best_k = 0
    best_score = 0
    for k in range(1, max_k+1):
        knn_model = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn_model, X_train, y_train, cv=5, scoring='accuracy')
        mean_score = scores.mean()
        if mean_score > best_score:
            best_score = mean_score
            best_k = k
    return best_k

# 2 veya daha fazla aykırı değer içeren satırları kaldırmak için bir fonksiyon tanımla
def remove_outliers(X, y):
   # Her sütun için çeyreklikleri hesapla
    q1 = np.percentile(X, 25, axis=0)
    q3 = np.percentile(X, 75, axis=0)
    # Her sütun için IQR'yi hesapla
    iqr = q3 - q1
    # Aykırı değerler için alt ve üst sınırları hesapla
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    # Her satırdaki aykırı değerlerin sayısını hesapla
    num_outliers = np.sum((X < lower_bound) | (X > upper_bound), axis=1)
    # 2'den fazla aykırı değer içeren satırları kaldır
    X_clean = X[num_outliers <= 2]
    y_clean = y[num_outliers <= 2]
    return X_clean, y_clean