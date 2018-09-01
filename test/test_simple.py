from schemerfuzzer.util import build
import json
import logging
from jsonschema import validate

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

 


def test_empty():
    json_schema = {}
    result = build(json_schema)
    validate(result.value, json_schema)

def test_string():
    json_schema = {"type": "string"}
    result = build(json_schema)
    logger.debug("... %s",result)
    validate(result.value, json_schema)

def test_string_length():
    json_schema = {
            "type": "string",
            "maxLength": 30,
            "minLength": 1
    }
    result = build(json_schema)
    logger.debug(result)
    validate(result.value, json_schema)

def test_string_pattern():
    json_schema = {
            "type": "string",
            "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"
    }
    result = build(json_schema)
    logger.debug("... %s",result)
    validate(result.value, json_schema)

def test_number():
    json_schema = {"type": "number"}
    result = build(json_schema)
    validate(result.value, json_schema)

def test_number_multiple_of():
    json_schema = {
            "type": "number",
            "multipleOf": 3.0
    }
    result = build(json_schema)
    logger.debug("multiple of ...%s", result)
    validate(result.value, json_schema)

def test_number_excl_min_max():
    json_schema = {
            "type": "number",
            "minimum": 0,
            "maximum": 2,
            "exclusiveMinimum": True,
            "exclusiveMaximum": True
    }
    result = build(json_schema)
    logger.debug("excl min = %s", result)
    validate(result.value, json_schema)

def test_bool():
    json_schema = {
            "type": "boolean"
    }
    result = build(json_schema)
    logger.debug("Boolval = %s", result)
    validate(result.value, json_schema)

def test_string_enum():
    json_schema = {
            "type": "string",
            "enum": ["John", "Paul", "Ringo", "George"]
    }
    result = build(json_schema)
    logger.debug("Enum = %s", result)
    validate(result.value, json_schema)

def test_object_additional():
    json_schema = {
            "type": "object",
            "properties": {
                "number": {
                    "type": "number" 
                },
                "street_name": { 
                    "type": "string"
                },
                "street_type": { 
                    "type": "string",
                    "enum": ["Street", "Avenue", "Boulevard"]
                }
            },
            "additionalProperties": False
    }
    result = build(json_schema)
    logger.debug("object value = %s", result)
    validate(result.value, json_schema)

def test_object_required():
    json_schema = {
            "type": "object",
            "properties": {
                "name":      { "type": "string" },
                "email":     { "type": "string" },
                "address":   { "type": "string" },
                "telephone": { "type": "string" }
            },
            "required": ["name", "email"]
    }
    result = build(json_schema)
    logger.debug("object value = %s", result)
    validate(result.value, json_schema)

def test_object_size():
    json_schema = {
            "type": "object",
            "minProperties": 2,
            "maxProperties": 3
    }
    result = build(json_schema)
    logger.debug("result = %s", result)
    validate(result.value, json_schema)
