import sys

def parser(file):
    counter = 1
    dns_count = 0
    for line in file:
        split_line = line.split(";")
        if len(split_line) < 4:
            continue
        src_ip = split_line[2]
        dst_ip = split_line[4]
        if src_ip == "8.8.8.8" or src_ip == "8.8.4.4":
            dns_count += counter
        if dst_ip == "8.8.8.8" or dst_ip == "8.8.4.4":
            dns_count += counter
    print(dns_count)

def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(parser(open_file))
    open_file.close()

main()