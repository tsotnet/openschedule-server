import sys
import json
import parse
import pprint
if len(sys.argv) != 2:
  print "The program must take only one argument - input file name"
  exit()

try:
  content = open(sys.argv[1]).read()
except:
  print "File not found"
  exit()
  
print parse.uploadFile(sys.argv[1], content)
