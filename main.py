import json
import os


def load_results(filename="results.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []


def save_results(results, filename="results.json"):
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)


def calculate_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def add_student(results):
    try:
        name = input("Enter student name: ")
        maths = int(input("Enter Maths marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))

        total = maths + science + english
        average = total / 3
        grade = calculate_grade(average)

        results.append({
            "name": name,
            "maths": maths,
            "science": science,
            "english": english,
            "total": total,
            "average": round(average, 2),
            "grade": grade
        })

        save_results(results)
        print("Student result added successfully!")
    except ValueError:
        print("Marks must be numbers.")


def view_results(results):
    if not results:
        print("No results available.")
        return

    print("\n--- Student Results ---")
    for r in results:
        print(
            f"{r['name']} | Total: {r['total']} | "
            f"Avg: {r['average']} | Grade: {r['grade']}"
        )


def show_topper(results):
    if not results:
        print("No data available.")
        return

    topper = max(results, key=lambda x: x["total"])
    print("\n🏆 Topper")
    print(f"{topper['name']} with {topper['total']} marks")


def show_menu():
    print("\n====== STUDENT RESULT ANALYZER ======")
    print("1. Add Student Result")
    print("2. View Results")
    print("3. Show Topper")
    print("4. Exit")


def result_analyzer_app():
    results = load_results()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(results)
        elif choice == "2":
            view_results(results)
        elif choice == "3":
            show_topper(results)
        elif choice == "4":
            print("Exiting Result Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


result_analyzer_app()
