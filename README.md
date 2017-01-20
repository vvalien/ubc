# UBC
aka... UnBreakableCrypto

At one point in time I wrote a whole bunch of info about this, however its fairly simple. If you can manage to generate truly random numbers this becomes a OneTimePad. Which means as long as you distribute the key file securily it can never be broken.

My suggestion is boot to a live OS not connected to the net, and generate a very large keyfile. Then burn 2 copies and hand one to your buddie the next time you see them in person. You can select which part of the keyfile you use with the -c option, this enabels you to use the same keyfile more than once since there is no harm in transmitting the starting point.

# NEVER USE THE SAME SECTION TWICE!!!

If you would like more info...

https://en.wikipedia.org/wiki/XOR_cipher

https://en.wikipedia.org/wiki/One-time_pad

I would suggest using the random number generator from pycrypto rather than Random 

https://pypi.python.org/pypi/pycrypto

# Generate A Keyfile
ubc.py -g -c 1000 -k master.key

# Encrypt A File
ubc.py -e -i infile.txt -k master.key -o outfile.crypt

# Decrypt A File
ubc.py -d -i infile.crypt -k master.key -o outfile.decrypt
