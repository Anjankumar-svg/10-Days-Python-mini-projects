def calculate_class_sgpa():
    # 1. Collection of student dictionaries
    students = [
        {
            "name": "ANIL KUMAR",
            "Mid": [48, 50, 40, 35],
            "sem": [50, 60, 68, 56],  # Matches 4 target courses
            "lab": [10, 9, 8]
        },
        {
            "name": "KISHORE KUMAR",
            "Mid": [54, 34, 23, 45],
            "sem": [56, 67, 58, 59],
            "lab": [9, 9, 9]
        },
        {
            "name": "SAI KUMAR",
            "Mid": [20, 8, 40, 46],
            "sem": [23, 45, 37, 9],
            "lab": [7, 8, 9]
        },
        {
            "name": "ARUN KUMAR",
            "Mid": [45, 50, 30, 40],
            "sem": [50, 55, 48, 52],
            "lab": [8, 7, 8]
        },
        {
            "name": "RAJESH KUMAR",
            "Mid": [30, 40, 35, 45],
            "sem": [40, 50, 45, 55],
            "lab": [7, 8, 9]
        }
    ]

    max_mid = 60
    max_sem = 70
    max_lab = 10

    credits = [4, 4, 4, 4] 

    for student in students:
        total_quality_points = 0
        total_credits = 0

        print(f"\nStudent_Name: {student['name']}")
        print("-" * 55)
        print(f"{'Course':<8}{'Mid':<6}{'Sem':<6}{'Lab':<6}{'Percentage':<12}{'Grade Point':<12}")
        print("-" * 55)

        for i in range(4):
            obtained = student["Mid"][i] + student["sem"][i]
            maximum = max_mid + max_sem
            if i < len(student["lab"]):
                obtained += student["lab"][i]
                maximum += max_lab
                lab_str = str(student["lab"][i])
            else:
                lab_str = "N/A"

            percentage = (obtained / maximum) * 100
            if percentage >= 90:
                gp = 10
            elif percentage >= 80:
                gp = 9
            elif percentage >= 70:
                gp = 8
            elif percentage >= 60:
                gp = 7
            elif percentage >= 50:
                gp = 6
            elif percentage >= 40:
                gp = 5
            elif percentage >= 35:
                gp = 4
            else:
                gp = 0  # Fail threshold

            print(f"{i+1:<8}{student['Mid'][i]:<6}{student['sem'][i]:<6}{lab_str:<6}{percentage:>.2f}%{'':<5}{gp:<12}")

            total_quality_points += gp * credits[i]
            total_credits += credits[i]
        sgpa = total_quality_points / total_credits
        print("-" * 55)
        print(f"Final SGPA for {student['name']}: {sgpa:.2f}")
        print("=" * 55)
calculate_class_sgpa()
