import joblib
rf=joblib.load('model/rfc.pkl') 

def predict(features):
    return rf.predict(features)