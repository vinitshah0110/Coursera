import sys
import csv

def find_email(filename):
    email_list = {}
    with open(filename) as file:
        lines = csv.reader(file)

        for line in lines:
            name = str(line[0].lower())
            email_list[name] = line[1]
    try:
        fullname = sys.argv[1] + " " + sys.argv[2]
        print(email_list.get(fullname.lower()))
    except IndexError:
        print('Missing parameters')

def main():
    find_email('employee_data.csv')

if __name__ == "__main__":
    main()