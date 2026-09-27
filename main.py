from data_cleaner import DataCleaner
from visualizer import Visualizer
from predictor import Predictor
from result_analyzer import ResultAnalyzer
import pandas as pd
from data_loader import DataLoader
loader = DataLoader()
data = loader.load_data("student_performance.csv")
print("Rows before cleaning:", len(data))
cleaner = DataCleaner()
data = cleaner.clean(data)
print("Rows after cleaning:", len(data))
print(data[["student_id", "total_score", "grade", "result"]].head(10))
analyzer = ResultAnalyzer()
average_score = analyzer.average_score(data)
print("Average total score:", average_score)
pass_count, fail_count = analyzer.count_results(data)
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)
grade_counts = analyzer.grade_counts(data)
print("\nNumber of students by grade:")
print(grade_counts)
visualizer = Visualizer()

visualizer.show_pass_fail_chart(pass_count, fail_count)

visualizer.show_grade_chart(grade_counts)
# Average score by study hours
study_analysis = data.groupby("weekly_self_study_hours")["total_score"].mean()
print("\nAverage score by study hours:")
print(study_analysis.head(10))
# Group students by study hours
data["study_group"] = pd.cut(
    data["weekly_self_study_hours"],
    bins=[-1, 10, 20, 30, 40],
    labels=["0-10 hours", "11-20 hours", "21-30 hours", "31-40 hours"]
)
study_group_analysis = data.groupby("study_group", observed=False)["total_score"].mean()
print("\nAverage score by study group:")
print(study_group_analysis)
# Study hours and average score chart
visualizer.show_study_hours_chart(study_group_analysis)
# Simple prediction function

predictor = Predictor()

prediction = predictor.predict_result(20, 90, 4)

print("\nPrediction for a sample student:", prediction)

# Compare study, attendance and participation for Pass and Fail students
comparison = analyzer.average_factors_by_result(data)
print("\nAverage factors by result:")
print(comparison)
# Test prediction with different students

student1 = predictor.predict_result(5, 60, 2)
student2 = predictor.predict_result(30, 95, 5)

print("\nPrediction Test 1:", student1)
print("Prediction Test 2:", student2)
