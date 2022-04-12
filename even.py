### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def is_even(file):
    result = ""
    for line in file.readlines():
        line = line.strip()
        if int(line) % 2 == 0:
            # print(str(line.strip()) + " True")
            result += str(line) + " True" + "\n"
        else:
            # print(str(line.strip()) + " False")
            result += str(line) + " False" + "\n"
    return result


### MAIN FUNCTION ###
def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(is_even(open_file))
    open_file.close()

main()