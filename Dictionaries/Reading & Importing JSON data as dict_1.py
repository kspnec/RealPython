import json

jsonData = '[{"FirstName" : "Bob", "LastName" : "Johnson"}, {"FirstName": "Andrew", "LastName" : "Brown"}]'

# if you want to parse JSON file, use json.load() function instead
parsedJson = (json.loads(jsonData)) 

"""
parsedJson is stored as list
# whereas, each item within parsedJson list is stored as dictionary
"""
print(parsedJson)
print(type(parsedJson)) 
#print(type(parsedJson[0])) 

#Reading values from list, and then fetch FirstName, LastName from dictionaries
for x in parsedJson:
    print(x["FirstName"], x["LastName"])