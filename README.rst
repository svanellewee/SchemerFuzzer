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

Also to read from stdin provide dash as input parameter::

    #! echo '{"type": "string"}' | schmrfzr --input - --output result_json.json
Result::

    #! cat result_json.json
    "xi9ujefa0nubtpgdgf9hw1"
