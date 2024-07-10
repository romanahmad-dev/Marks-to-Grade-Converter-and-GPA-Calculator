def calculate_grade_percentage(marks_obtained, max_marks):
    return (marks_obtained / max_marks) * 100

def get_grade_and_gp(percentage):
    if percentage >= 85:
        return 'A', 4.0
    elif percentage >= 80:
        return 'A-', 3.7
    elif percentage >= 75:
        return 'B+', 3.3
    elif percentage >= 70:
        return 'B', 3.0
    elif percentage >= 65:
        return 'B-', 2.7
    elif percentage >= 61:
        return 'C+', 2.3
    elif percentage >= 58:
        return 'C', 2.0
    elif percentage >= 55:
        return 'C-', 1.7
    elif percentage >= 50:
        return 'D', 1.0
    else:
        return 'F', 0.0

def calculate_gpa(grades_points, credit_hours):
    total_points = sum(gp * ch for gp, ch in zip(grades_points, credit_hours))
    total_credit_hours = sum(credit_hours)
    return total_points / total_credit_hours

def calculate_cgpa(current_gpa, current_credit_hours, previous_gpa, previous_credit_hours):
    total_points = (current_gpa * current_credit_hours) + (previous_gpa * previous_credit_hours)
    total_credit_hours = current_credit_hours + previous_credit_hours
    return total_points / total_credit_hours

def main():
    print("Choose the grading system: ")
    print("1. Out-of 80")
    print("2. Out-of 60")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        max_marks = 80
    elif choice == 2:
        max_marks = 60
    else:
        print("Invalid choice.")
        return

    subjects = int(input("Enter the number of subjects: "))
    marks_list = []
    credit_hours = []

    for i in range(subjects):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        credits = float(input(f"Enter credit hours for subject {i+1}: "))
        marks_list.append(marks)
        credit_hours.append(credits)

    grades_points = []

    for i, marks in enumerate(marks_list):
        percentage = calculate_grade_percentage(marks, max_marks)
        grade, gp = get_grade_and_gp(percentage)
        grades_points.append(gp)
        print(f"Subject {i+1}: Marks = {marks}/{max_marks}, Percentage = {percentage:.2f}%, Grade = {grade}, Grade Point = {gp}")

    # Calculate GPA
    gpa = calculate_gpa(grades_points, credit_hours)
    print(f"Current Semester GPA: {gpa:.2f}")

    # Optionally calculate CGPA if previous GPA and credit hours are provided
    previous_gpa = float(input("Enter your previous GPA (or 0 if not applicable): "))
    previous_credit_hours = float(input("Enter your previous total credit hours (or 0 if not applicable): "))

    if previous_gpa > 0 and previous_credit_hours > 0:
        cgpa = calculate_cgpa(gpa, sum(credit_hours), previous_gpa, previous_credit_hours)
        print(f"Total CGPA: {cgpa:.2f}")
    else:
        print("Total CGPA: N/A")

if __name__ == "__main__":
    main()
