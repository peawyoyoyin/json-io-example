import json

obj = {"name":"foo", "number":7, "array":[1,2,3]}

jsontext = json.dumps(obj,indent=4,separators=(',', ':'))

f = open("example.json",'w')
f.write(jsontext)
f.close()
