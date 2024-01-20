from sklearn.metrics import classification_report, confusion_matrix

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