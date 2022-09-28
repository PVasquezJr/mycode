#!/usr/bin/env python3
def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    
    print(proto)

    proto.append("dns")
    print(proto)
    print(protoa)
    protoa.append("dns")

    proto2 = [22, 80, 443, 53]
    proto.extend(proto2)
    protoa.append(proto2)
    print(proto)
    print(protoa)

    proto.remove("ssh")
    print(proto.count("ssh"))                                       
    proto.reverse()
    print(proto)

main()
