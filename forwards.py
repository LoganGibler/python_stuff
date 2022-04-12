### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def forwards_is_backwards(file):
    result = ""
    for line in file.readlines():
        line = line.strip()
        
    return result



### MAIN FUNCTION ###
def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(forwards_is_backwards(open_file))
    open_file.close()
    
main()