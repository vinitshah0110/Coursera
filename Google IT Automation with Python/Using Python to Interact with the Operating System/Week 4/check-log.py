import sys
import os
import re

def error_search(log_file):
    error = input('Enter Error:')
    returned_errors = []

    with open(log_file, encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for item in range(len(error.split(' '))):
                error_patterns.append(r'{}'.format(error.split(' ')[item].lower()))
            
            if all(re.search(error, log.lower()) for error in error_patterns):
                returned_errors.append(log)
        file.close()
    print(returned_errors)

if __name__ == "__main__":

    log_file = sys.argv[1]
    error_search(log_file)