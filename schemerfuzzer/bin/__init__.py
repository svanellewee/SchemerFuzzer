from schemerfuzzer.util import build
import json
import argparse
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--input",
            type=argparse.FileType('r'),
            default='-',
            help="input json schema file or '-' to read from stdin"
    )
    parser.add_argument(
            "--output",
            type=argparse.FileType('w'),
            default='-',
            help="output json data"
    )
    parser.add_argument(
            "--verbose",
            help="verbose output?",
            action="store_true"
    )
    args = parser.parse_args()
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)
    logger.info(
            "input = %s, logger = %s, verbose = %s",
            args.input,
            args.output,
            args.verbose
    )
    
    json_schema = json.load(args.input)
    result = build(json_schema)
    json.dump(result.value, args.output)


if __name__ == "__main__":
    main()
