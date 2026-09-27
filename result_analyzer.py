class ResultAnalyzer:

    def average_score(self, data):
        return data["total_score"].mean()

    def count_results(self, data):
        pass_count = (data["result"] == "Pass").sum()
        fail_count = (data["result"] == "Fail").sum()

        return pass_count, fail_count

    def grade_counts(self, data):
        return data["grade"].value_counts()

    def average_factors_by_result(self, data):
        return data.groupby("result")[
            [
                "weekly_self_study_hours",
                "attendance_percentage",
                "class_participation"
            ]
        ].mean()
