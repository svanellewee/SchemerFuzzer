import logging
import pprint
import random
import string

import sre_yield

logger = logging.getLogger(__name__)


class Boolean(object):
    def __init__(self, schema):
        self.schema = schema
        self._compile()

    def _compile(self):
        self._value = random.choice([True, False])

    def __str__(self):
        return "true" if self._value else "false"

    @property
    def value(self):
        return self._value


class Array(object):
    def __init__(self, schema):
        self.schema = schema
        self._compile()

    def _compile(self):
        self.min_items = self.schema.get('minItems', 0)
        self.unique_items = bool(self.schema.get('uniqueItems'))

        self._value = set() if self.unique_items else list()
        while len(self._value) < self.min_items:
            self._value += [build(self.schema['items'])]

    @property
    def value(self):
        return [v.value for v in self._value]

    def __str__(self):
        item_list = ",".join(str(i) for i in self.items)
        return "{item_list}"


class String(object):
    def __init__(self, schema):
        self.valid_range = schema.get('valid_range')
        self.schema = schema
        self.pattern = schema.get('pattern')
        self.min_length = self.schema.get('minLength', 1)
        self.max_length = self.schema.get('maxLength', 100)
        if self.min_length > self.max_length:
            raise ValueError("Min length should not be Larger than max")
        self.enum = schema.get('enum', set())
        is_string = lambda value: isinstance(value, str)
        if not all(is_string(e) for e in self.enum):
            raise ValueError("Enums must all be strings")

    @property
    def value(self):
        if len(self.enum) != 0:
            return random.choice(self.enum)
        logger.debug("SCHEMA= %s", pprint.pformat(self.schema))
        # import pdb; pdb.set_trace()
        if self.pattern:
            pattern = sre_yield.AllStrings(self.pattern)
            logger.debug("%s.. %s!!", self.min_length, self.max_length)
            _value = pattern[random.randint(0, pattern.length)]
        else:
            _value = rand_chars(random.randint(self.min_length, self.max_length))
        logger.debug(f".{_value}")
        return _value

    def __str__(self):
        return self.value


class Number(object):
    def __init__(self, schema):
        self.schema = schema
        self._compile()

    def _compile(self):
        self.minimum = self.schema.get('minimum', -100.0)
        self.maximum = self.schema.get('maximum', 100.0)
        self.multiple_of = self.schema.get('multipleOf')
        self.exclusive_minimum = self.schema.get('exclusiveMinimum')
        self.exclusive_maximum = self.schema.get('exclusiveMaximum')
        minimum = self.minimum
        if self.exclusive_minimum:
            minimum += 1
        maximum = self.maximum
        if self.exclusive_maximum:
            maximum -= 1
        self._value = float(random.randint(minimum, maximum))
        if self.multiple_of:
            self._value *= self.multiple_of
        if self.minimum > self.maximum:
            raise ValueError("Min should not be Larger than max")

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self._value)


class Integer(object):
    def __init__(self, schema):
        self.schema = schema
        self._compile()

    def _compile(self):
        self.minimum = self.schema.get('minimum', -100)
        self.maximum = self.schema.get('maximum', 100)
        self._value = random.randint(self.minimum, self.maximum)
        if self.minimum > self.maximum:
            raise ValueError("Min should not be larger than max")

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)


def rand_chars(number=1):
    result = []
    for i in range(number):
        result += [random.choice(string.ascii_lowercase + string.digits)]
    return "".join(result)


class Object(object):
    def __init__(self, schema):
        self.schema = schema
        self._compile()

    def _compile(self):
        self.required = self.schema.get('required', [])
        self.additional_properties = self.schema.get('additionalProperties', True)
        self.properties = {}
        if 'properties' in self.schema:
            for name, sub_schema in self.schema['properties'].items():
                self.properties[name] = build(sub_schema)
            for required in self.required:
                if required not in self.properties:
                    raise ValueError(f"Required field {required} missing")
        elif 'minProperties' in self.schema or 'maxProperties' in self.schema:
            min_props = self.schema.get('minProperties', 0)
            max_props = self.schema.get('maxProperties', 0)
            num_vals = random.randint(min_props, max_props)
            for i in range(num_vals):
                schema_type = random.choice([k for k in lookups.keys() if k is not 'array'])
                self.properties[rand_chars(5)] = build({"type": schema_type})

    def _handle_additional_properties(self):
        pass

    def __getattr__(self, name):
        return self.properties[name]

    @property
    def value(self):
        result = {name: value.value
                  for name, value in self.properties.items()}
        return result

    def __str__(self):
        prop_dict = ",\n".join(f"{name}: {str(value)}" for name, value in self.properties.items())
        return f"{ {prop_dict} }"


lookups = {
    "object": Object,
    "integer": Integer,
    "number": Number,
    "array": Array,
    "string": String,
    "boolean": Boolean
}


def build(schema):
    _type = schema.get('type')
    if not _type:
        return Integer({"type": "integer"})
    cur_type = lookups[_type]
    return cur_type(schema)
