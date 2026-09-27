# Student Exam Results Analysis System

## Project Description

The Student Exam Results Analysis System is a Python application developed for Bright Future School.

The system analyses a large student performance dataset containing 1,000,000 student records.

## Main Features

- Loads student performance data from a CSV file.
- Removes duplicate and missing data.
- Calculates the average student score.
- Identifies Pass and Fail results.
- Analyses student grades.
- Analyses the relationship between study hours and scores.
- Displays charts for student performance.
- Provides a simple rule-based prediction of Pass or Fail.
- Includes automated tests using Pytest.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Pytest

## Project Structure

```text
StudentResultsApplication/
├── student_performance.csv
├── main.py
├── data_loader.py
├── data_cleaner.py
├── result_analyzer.py
├── visualizer.py
├── predictor.py
├── requirements.txt
├── README.md
└── tests/
    └── test_application.py
```
