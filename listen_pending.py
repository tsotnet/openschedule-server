import parse
import time
import user

timer = 5 # check Pending database every [timer] seconds

while True:
  t1 = time.time()
  pending = parse.getObjects('Pending')
  if pending == None:
    break
  for i in pending["results"]:
    print i["username"], i["password"]
    u = user.User(i["username"], i["password"])
    if u.authenticate() == True:
      USER = parse.signUp(i["username"], i["password"])
      if USER == None or USER.has_key("error"):
        parse.removeObject('Pending', i["objectId"])
        continue
      s = u.getSubjectListing()
      parse.createObject("UserInfo",
                         {
                           "username": i["username"],
                           "subjects": s,
                           "ACL": {
                             USER["objectId"]: {
                              "read": True,
                              "write": True
                             }
                           }
                         })
    # It's important for client to check 
    parse.removeObject('Pending', i["objectId"])
  t2 = time.time()
  if t2-t1<timer:
    time.sleep(timer-t2+t1)
  t2 = time.time()
  print t2-t1

