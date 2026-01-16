import pandas as pd
import joblib

class AIDecisionEngine:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

        # 🔒 Define feature contract (VERY IMPORTANT)
        self.model_features = ["accuracy", "avg_time", "attempts"]

    def rule_based(self, data):
        if data["accuracy"] >= 0.8 and data["avg_time"] <= 20:
            return "Advance"
        return "Revise"

    def ml_based(self, data):
        # ✅ Filter ONLY the features used during training
        filtered_data = {k: data[k] for k in self.model_features}

        df = pd.DataFrame([filtered_data])
        pred = self.model.predict(df)[0]
        return "Advance" if pred == 1 else "Revise"
