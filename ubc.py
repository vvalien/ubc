#!/usr/bin/python
import sys
import argparse
import random as rnd

# randomness is the only issue
def gen_key(key_len):
    ret = []
    for i in range(key_len):
        ret.append(chr(rnd.randint(0, 255)))
    return ''.join(ret)

def ubc(data, key, pos):
    ret = []
    if len(key[pos:]) < len(data):
        print("Key is smaller than data...")
        sys.exit()
    for i in range(len(data)):
        ret.append(chr(ord(data[i]) ^ ord(key[pos + i])))
    return ''.join(ret)

def filetobytes(fname):
    t = open(fname, "rb")
    ret = t.read()
    t.close()
    return ret
    
def bytestofile(fname, data):
    t = open(fname, "wb")
    t.write(data)
    t.close()

if __name__ == "__main__":
    usage_text = "ubc.py -g -c 1000 -k master.key\n"
    usage_text += "usage: ubc.py -e -i infile.txt -k master.key -o outfile.crypt\n"
    usage_text += "usage: ubc.py -d -i infile.crypt -k master.key -o outfile.decrypt"
    parser = argparse.ArgumentParser(usage=usage_text)
    parser.add_argument('-k', help='Key File')
    parser.add_argument('-i', help='Input File')
    parser.add_argument('-o', help='Output File')
    parser.add_argument('-c', default=0, type=int, help='Count or Position')
    parser.add_argument('-g', action="store_true", default=False, help='Generate')
    parser.add_argument('-e', action="store_true", default=False, help='Encrypt')
    parser.add_argument('-d', action="store_true", default=False, help='Decrypt')
    nargs = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()  
    if nargs.g and nargs.c and nargs.k:
        ret = gen_key(nargs.c)
        bytestofile(nargs.k, ret)
        print("Generated your keyfile")
    if nargs.e and nargs.i and nargs.k and nargs.o:
        t = filetobytes(nargs.i)
        k = filetobytes(nargs.k)
        r = ubc(t, k, nargs.c)
        bytestofile(nargs.o, r)
        print("Used section %d:%d of keyfile" % (nargs.c, (nargs.c + len(t))))
    if nargs.d and nargs.i and nargs.k and nargs.o:
        t = filetobytes(nargs.i)
        k = filetobytes(nargs.k)
        r = ubc(t, k, nargs.c)
        bytestofile(nargs.o, r)
        print("Used section %d:%d of keyfile" % (nargs.c, (nargs.c + len(t))))
