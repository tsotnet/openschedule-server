import sys
import json
import parse
import pprint
if len(sys.argv) != 2:
  print "The program must take only one argument - input file name"
  exit()
subjects = json.load(open(sys.argv[1]))
# Subjects is a dictionary, where each key describes a class. Example:
# "6.816" -> {
# number:       "6.816"
# name:         "Multicore Programming"
# description:  "bla bla bla"
# lectures:     ["L01 TR3-4.30 6-120"]
# recitations:  ["F10 36-112 R01", ... ,"F12 36-112 R03", ...]
# labs:         []
# }
counter = 0
for i in subjects.keys():
  subject = subjects[i].copy()
  # subject["ACL"] = {}
  print counter
  counter+=1
  print parse.createObject("Subjects", subject)
                  
#print parse.retrieveObject("Pending", "gm4wrAvXBy")
