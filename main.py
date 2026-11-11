
import csv
import os
from datetime import date

STUDENTS_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"


def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    students = []
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            students = list(csv.reader(f))

    if any(row[0] == sid for row in students):
        print("Student ID already exists!")
        return

    with open(STUDENTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sid, name])

    print("Student added successfully!")


def view_students():
    if not os.path.exists(STUDENTS_FILE):
        print("No students found!")
        return

    with open(STUDENTS_FILE, "r") as f:
        students = list(csv.reader(f))

    print("\n--- Student List ---")
    for student in students:
        print("ID:", student[0], "| Name:", student[1])


def mark_attendance():
    sid = input("Enter Student ID: ")

    if not os.path.exists(STUDENTS_FILE):
        print("No students found!")
        return

    with open(STUDENTS_FILE, "r") as f:
        students = list(csv.reader(f))

    student = next((s for s in students if s[0] == sid), None)

    if student is None:
        print("Student not found!")
        return

    status = input("Enter P for Present or A for Absent: ").upper()

    if status not in ["P", "A"]:
        print("Invalid attendance!")
        return

    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sid, student[1], str(date.today()), status])

    print("Attendance marked successfully!")


def view_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found!")
        return

    with open(ATTENDANCE_FILE, "r") as f:
        records = list(csv.reader(f))

    print("\n--- Attendance Records ---")
    for row in records:
        print("ID:", row[0], "| Name:", row[1],
              "| Date:", row[2], "| Status:", row[3])


def main():
    while True:
        print("\n===== STUDENT ATTENDANCE SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
