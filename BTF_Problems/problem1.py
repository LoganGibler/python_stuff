import sys

def parser(file):
    counter = 1
    srcIPobj = {}
    dstIPobj = {}
    combinedIps = {}

    for line in file:
        split_line = line.split(";")
        if len(split_line) < 4:
            continue
        src_ip = split_line[2]
        dst_ip = split_line[4]

        if src_ip not in combinedIps:
            combinedIps[src_ip] = counter
        else:
            combinedIps[src_ip] += counter

        if dst_ip not in combinedIps:
            combinedIps[dst_ip] = counter
        else:
            combinedIps[dst_ip] += counter

        if src_ip not in srcIPobj:
            srcIPobj[src_ip] = counter
        else:
            srcIPobj[src_ip] += counter
         
        if dst_ip not in dstIPobj:
            dstIPobj[dst_ip] = counter
        else:
            dstIPobj[dst_ip] += counter

        sortedCombinedIps = sorted(combinedIps, key=combinedIps.get)
        sortedCombinedDic = {}

        sortedSrcIPs = sorted(srcIPobj, key=srcIPobj.get)
        sortedSrcDic = {}

        sortedDstIPs = sorted(dstIPobj, key=dstIPobj.get)
        sortedDstDic = {}
        for i in sortedCombinedIps:
            sortedCombinedDic[i] = combinedIps[i]
        for i in sortedSrcIPs:
            sortedSrcDic[i] = srcIPobj[i]
        for i in sortedDstIPs:
            sortedDstDic[i] = dstIPobj[i]

    print("all ips", sortedCombinedDic)
    print("src ips: ", sortedSrcDic)
    print("dst ips: ", sortedDstDic)

def main():
    file_name = sys.argv[1]
    open_file = open(file_name, "r")
    print(parser(open_file))
    open_file.close()

main()