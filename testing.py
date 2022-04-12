import sys

def test_func(file):
    for line in file.readlines():
        line = line.strip()
        print(line)
        
def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(test_func(open_file))
    open_file.close()
    
main()