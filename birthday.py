import sys


# helper functions
def birthday_party(file):
    dict1 = {}
    result = ""
    for line in file.readlines():
        line = line.strip()
        if line not in dict1:
            dict1[line] = 1
        else:
            dict1[line] += 1
    
    sorted_names = sorted(dict1.keys())
    
    for i in sorted_names:
        result += i + " - " + str(dict1[i])
        if i not in sorted_names[-1]:
            result += "\n"
            
    return result
# main function
def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(birthday_party(open_file))
    open_file.close()

main()