from visualizer import Visualizer
from result_analyzer import ResultAnalyzer
from data_cleaner import DataCleaner
import pandas as pd
from predictor import Predictor


def test_pass_prediction():
    predictor = Predictor()

    result = predictor.predict_result(20, 90, 4)

    assert result == "Pass"


def test_fail_prediction():
    predictor = Predictor()

    result = predictor.predict_result(5, 60, 2)

    assert result == "Fail"


def test_data_cleaning():
    data = pd.DataFrame({
        "total_score": [80, 40, 80],
        "student_id": [1, 2, 1]
    })

    cleaner = DataCleaner()
    cleaned_data = cleaner.clean(data)

    assert len(cleaned_data) == 2
    assert cleaned_data.iloc[0]["result"] == "Pass"
    assert cleaned_data.iloc[1]["result"] == "Fail"


def test_average_score():
    data = pd.DataFrame({
        "total_score": [80, 60, 100]
    })

    analyzer = ResultAnalyzer()

    result = analyzer.average_score(data)

    assert result == 80


def test_count_results():
    data = pd.DataFrame({
        "result": ["Pass", "Pass", "Fail", "Pass", "Fail"]
    })

    analyzer = ResultAnalyzer()

    pass_count, fail_count = analyzer.count_results(data)

    assert pass_count == 3
    assert fail_count == 2


def test_visualizer_methods():
    visualizer = Visualizer()

    assert hasattr(visualizer, "show_pass_fail_chart")
    assert hasattr(visualizer, "show_grade_chart")
