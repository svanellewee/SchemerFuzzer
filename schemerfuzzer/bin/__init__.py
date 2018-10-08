from schemerfuzzer.util import build
import json
import argparse
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=argparse.FileType(), help="input json schema file or '-' to read from stdin",
                        required=True)
    parser.add_argument("--output", help="output json data", required=True)
    parser.add_argument("--verbose", help="verbose output?", action="store_true")
    args = parser.parse_args()
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)
    logger.info("input = %s, logger = %s, verbose = %s", args.input, args.output, args.verbose)
    with open(args.output, 'w') as result_file:
        json_schema = json.load(args.input)
        result = build(json_schema)
        json.dump(result.value, result_file)

if __name__ == "__main__":
    main()
