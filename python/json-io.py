import json

#input
file = open("../example.json")

text = file.read()

read_object = json.loads(text)
for key in read_object:
    print(key, read_object[key])

file.close()

#output
file = open("example-write.json",'w')

obj_to_write = { "foo":"bar", "baz":7, "qux":[1,2,3] }

file.write(json.dumps(obj_to_write, indent=4, separators=(',',':')))
file.close()
