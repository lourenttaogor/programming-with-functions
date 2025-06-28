import csv

def read_dictionary(filename, key_column_index):
    s_dictionary = {}
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            key = row[key_column_index]
            s_dictionary[key] = row

    return s_dictionary
def main():
    key_column_index = 0  # Assuming the first column is the key 
    name_index = 1  # Assuming the second column is the name
    students = read_dictionary('students.csv', key_column_index)
    inumber = input("Please enter a student's I-Number: ")
    inumber = inumber.replace("-", "")  # Remove any hyphens if present
    if not inumber.isdigit():
        print("Invalid I-Number format. Please enter a valid I-Number.")
    elif len(inumber) != 9:
        print("Inumber too shortr. Please enter a 9-digit I-Number.")
    elif len(inumber) > 9:
        print("Inumber too long. Please enter a 9-digit I-Number.")
    else:
        print("Please enter a student's I-Number: ")
    if inumber in students:
        student = students[inumber]
        name = student[name_index]
        print(f"The name of the student with I-Number {inumber} is {name}.")
    else:
        print("No such student found with that I-Number.")
    

if __name__ == "__main__":
    main()
