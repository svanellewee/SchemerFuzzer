===============
SchemerFuzzer
===============


SchemerFuzzer uses JSON Schema to generate randomized json. 

Simple Regex example::
   
    #! cat examples/test-regex.json
    {"type": "string", "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$" }

In order to test here's an example::

    #! schmrfzr  --input examples/jsonschema.txt --output result_json.json

Will result in something that looks like::

    #! cat result_json.json
    "(071)569-3221"

