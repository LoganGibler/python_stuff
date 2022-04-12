
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def counter(file):
    ip_object = {}
    count = 0
    result = ""
    for line in file.readlines():
        line = line.strip()
        string_split = line.split(" -")
        ip_string = string_split[0]
        if ip_string not in ip_object:
            count = 1
            ip_object[ip_string] = count
        else:
            count = 1
            ip_object[ip_string] += count
    sorted_ips = sorted(ip_object.keys())
    for i in sorted_ips:
        result += i + " - " + str(ip_object[i])
        if i not in sorted_ips[-1]:
            result += "\n"
    return result


### MAIN FUNCTION ###
def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(counter(open_file))
    open_file.close()
    
main()