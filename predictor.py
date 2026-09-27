class Predictor:
    def predict_result(self, study_hours, attendance, participation):
        score = (
            study_hours * 1.5
            + attendance * 0.5
            + participation * 2
        )
        if score >= 60:
            return "Pass"
        else:
            return "Fail"
