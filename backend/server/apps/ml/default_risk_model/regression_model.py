# file backend/server/apps/ml/default_risk_model/regression_model.py
import joblib
import pandas as pd

class defaultClassifier:
    def __init__(self):
        path_to_artifacts = "../../research/"
        self.values_fill_missing =  joblib.load(path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "regressor.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data,index=[0])
      
      
        return input_data

    def predict(self, input_data):
        return self.model.predict(input_data)

    def postprocessing(self, input_data):
         label = "No Default"
        if input_data[1] > 0.5:
            label = "Default"
        return {"probability": input_data[1], "label": label, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction