import sys
import hashlib

if len(sys.argv) != 2:
	print "Usage: strinttohash.py <string>"
	sys.exit()

m = hashlib.md5()
m.update(sys.argv[1])
print m.hexdigest()