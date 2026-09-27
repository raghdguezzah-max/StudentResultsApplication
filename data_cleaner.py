class DataCleaner:

    def clean(self, data):
        data = data.drop_duplicates()

        data = data.dropna()

        data["result"] = data["total_score"].apply(
            self._calculate_result
        )

        return data

    def _calculate_result(self, score):
        if score >= 50:
            return "Pass"

        return "Fail"
