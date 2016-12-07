text = '{ \
    "number":7, \
    "array":[ \
        1, \
        2, \
        3 \
    ], \
    "name":"foo" \
}'

console.log(JSON.parse(text));

output = document.getElementById("JSONtext");

objToWrite = {foo:"bar", baz:7, qux:[1,2,3]};

console.log(JSON.stringify(objToWrite));

output.innerHTML = JSON.stringify(objToWrite);
