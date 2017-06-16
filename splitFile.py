#!/usr/bin/env python3
import struct
import sys


def toBytes(input):
    # input is xxxxKB, xxxxMB, xxxxGB...
    si = input[-2:].upper()
    val = float(input[:-2])
    if si == "KB":
        val = val * 1024
    elif si == "MB":
        val = val * 1024**2
    elif si == "GB":
        val = val * 1024**3
    elif si == "TB":
        val = val * 1024**4
    elif si == "PB":
        val = val * 1024**5
    else:
        print("ERROR: Please set width about KB~PB")
    return int(val)


def openFile(filename, length="1KB"):
    with open(filename, "rb") as bfile:
        bdata = bfile.read()
        times = int(len(bdata)/toBytes(length))
        print(times)
        i = 0
        while True:
            if i > times:
                break;
                
            print("now",i)
            bfile.seek(i*toBytes(length))
            bdata = bfile.read()
            with open("{}.{}.spf".format(filename, i), "wb+") as newbfile:
                newbfile.write(bdata)
            i+=1;
    


openFile(sys.argv[1])
