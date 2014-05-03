import json
import httplib

openschedule_credentials = {
         "X-Parse-Application-Id": "roVXtrENMwnxSkc1wQaFZrDRZMMNp1tbi9pFpTeq",
#         "X-Parse-REST-API-Key": "eG91hhYXEsx2NWUsAEDYAB2KAzvE9MrvJgfjiuuH",
         "X-Parse-Master-Key": "m6fZZrdOzk8zVd6xaALGh8In8mWjyia6WRVu9IjY",
         "Content-Type": "application/json"
       }

# Cloud Code
def callCloudCode(function_name, params):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST',
                       '/1/functions/'+function_name,
                       json.dumps(params),
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None
  
# Object Manipulation (Create, Get, Find, Remove, etc.)
def createObject(class_name, params):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST',
                       '/1/classes/'+class_name,
                       json.dumps(params),
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None
    
def getObject(class_name, object_name):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET',
                       '/1/classes/'+class_name+'/'+object_name,
                       '',
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None
    
def removeObject(class_name, object_name):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('DELETE',
                       '/1/classes/'+class_name+'/'+object_name,
                       '',
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None



    
# Queries (https://parse.com/docs/rest#queries-constraints)
def getObjects(class_name):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET',
                       '/1/classes/'+class_name,
                       '', 
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None

def getObjectsWithParams(class_name, params):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"where":json.dumps(params)})
    connection.connect()
    connection.request('GET',
                       '/1/classes/'+class_name+'?%s' % params,
                       '',
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None
    
    
    
    
# Users
def signUp(username, password):
  try:
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST',
                       '/1/users',
                       json.dumps({
                         "username": username,
                         "password": password,
                       }),
                       openschedule_credentials)
    return json.loads(connection.getresponse().read())
  except:
    return None
