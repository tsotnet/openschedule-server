import json
import re
from pprint import pprint

counter = 0

def convert(s):
  dbg, ss = False, s
  s = s.split()
  a = s[0] # L01
  c = s[-1] # 34-101
  # MW EVE (7-8.30 PM)
  # MW8.30-10 (ENDS MARCH 14)
  # TR8.30-10 (BEGINS MARCH 31)
  # MW9-11
  b = " ".join(s[1:-1])
  global counter
  if (not re.match("M?T?W?R?F?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)?$", b) and # MWF11 # MW8.30-10.30
      not re.match("M?T?W?R?F? EVE \([0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)? PM\)?$", b) and #M EVE (7-9 PM) #MW EVE (7 PM)
      not re.match("M?T?W?R?F?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)?(,M?T?W?R?F?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)?)?$", b) and # M1,W2
      not re.match("M?T?W?R?F?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)? \(BEGINS [A-Z]+ [0-9]+\)$", b) and
      not re.match("M?T?W?R?F?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)? \(ENDS [A-Z]+ [0-9]+\)$", b)):
      
    counter+=1
    print ss
#  s = b.split()
#  if len(s) > 1:
#    dbg = True
#    if s[1] == "EVE":
#      b = s[0]+s[2][1:]
  s = " ".join([a,b,c])
#  if dbg:
#    print s
#    print ss
  return s
  

# The file was acquired from http://coursews.mit.edu/coursews/?term=2014SP
data = json.load(open("subjects_sp2014.json"))
items = data["items"]
subjects = {}
for i in items:
  if i["type"] == "Class":
    subjects[i["id"]] = c = {}
    c["number"] = i["id"]
    c["name"] = i["label"]
    c["description"] = i["description"]
    c["lectures"] = []
    c["recitations"] = []
    c["labs"] = []

for i in items:
  if (i["type"] == "Class" or
      i["timeAndPlace"].find("ARRANGED")!=-1 or
      i["timeAndPlace"].find("null")!=-1 or
      i["timeAndPlace"].find("TBD")!=-1):
    continue
  number = i["section-of"]
  info = convert(i["label"][:3]+" "+i["timeAndPlace"])
  if info == None:
    continue
  if i["type"] == "LectureSession":
    subjects[number]["lectures"].append(info)
  elif i["type"] == "RecitationSession":
    subjects[number]["recitations"].append(info)
  elif i["type"] == "LabSession":
    subjects[number]["labs"].append(info)
  else:
    print "ERROR "+i["type"]

for i in subjects:
  k = subjects[i]
  for j in (k["lectures"]+k["recitations"]+k["labs"]):
    s = " ".join(j.split())
    if len(s.split(" ")) != 3:
      continue
      print j
      print s
#      exit()

print counter
#with open("subjects_sp2014_parsed.json", "w") as File:
#  json.dump(subjects, File)
#pprint (subjects["6.816"])

#print callParseCloudCode("hello", {"print_value": "gamarjoba"})["result"]
