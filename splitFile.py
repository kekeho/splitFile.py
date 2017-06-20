#!/usr/bin/env python3
from glob import glob
from os import path


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


def split(filename, length="1MB"):
    try:
        with open(filename, "rb") as bfile:
            times = int(path.getsize(filename) / toBytes(length))
            i = 0
            while True:
                if i > times:
                    break
                bdata = bfile.read(toBytes(length))
                with open("{}.{}.spf".format(filename, i), "wb") as splitfile:
                    splitfile.write(bdata)
                i += 1
            print("done! create {} spf files.".format(times))
    except FileNotFoundError:
        print("No such file: '{}'".format(filename + 1))


def join(directory=""):
    if directory != "":
        if directory[:-1] != "/":
            directory = directory + "/"
    allSpfFiles = sorted(glob("{}*.spf".format(directory)))
    print(allSpfFiles)
    for filename in allSpfFiles:
        try:
            with open(filename, "rb") as bfile:
                with open(filename.rsplit(".", 2)[0], "ab") as joinedfile:
                    joinedfile.write(bfile.read())
        except FileNotFoundError:
            print("No such '.spf' file.")


if __name__ == '__main__':
    import sys, re
    argv = sys.argv
    
    r = re.compile("-byte=")
    
    if argv.count('-j') == 1:
        if len(argv) == 3:
            join(argv[2])
        else:
            join()
    elif [x for x in argv if r.match(x)]:
        split(argv[1], [x for x in argv if r.match(x)][0][6:])
