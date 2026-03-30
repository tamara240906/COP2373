import csv
# Create CVS file
def write_grades():
    # Ask how many students the instructor wants to enter
    num_students = int(input("Enter number of students: "))

    # Open file in write mode
    with open("grades.csv", "w", newline='') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student
        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}")

            # Get student info
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            # Get exam scores
            exam1 = int(input("Enter Exam 1 score: "))
            exam2 = int(input("Enter Exam 2 score: "))
            exam3 = int(input("Enter Exam 3 score: "))

            # Write student record to CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\nData successfully written to grades.csv!")


#Read and display CSV file
def read_grades():
    # Open file in read mode
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        print("\n--- Student Grades ---\n")

        # Loop through rows and print in table format
        for row in reader:
            # Format each column with spacing
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<8} {row[3]:<8} {row[4]:<8}")


# Main program
def main():
    write_grades()
    read_grades()

# Call main
main()