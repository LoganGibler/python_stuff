### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def haiku(file):
    js_object = {}
    for line in file.readlines():
        line = line.strip()
        string_split = line.split(", ")
        print(string_split[0])
        
        
        



### MAIN FUNCTION ###
def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(haiku(open_file))
    open_file.close()
  
main()  
