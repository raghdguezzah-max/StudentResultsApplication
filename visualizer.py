import matplotlib.pyplot as plt


class Visualizer:

    def show_pass_fail_chart(self, pass_count, fail_count):
        labels = ["Pass", "Fail"]
        values = [pass_count, fail_count]

        plt.bar(labels, values)

        plt.title("Student Pass and Fail Results")
        plt.xlabel("Result")
        plt.ylabel("Number of Students")

        plt.show()

    def show_grade_chart(self, grade_counts):
        grade_counts.plot(kind="bar")

        plt.title("Student Grade Distribution")
        plt.xlabel("Grade")
        plt.ylabel("Number of Students")

        plt.show()

    def show_study_hours_chart(self, study_group_analysis):
        study_group_analysis.plot(kind="bar")
        plt.title("Average Score by Weekly Study Hours")
        plt.xlabel("Weekly Self-Study Hours")
        plt.ylabel("Average Total Score")
        plt.show()
