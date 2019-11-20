import argparse
import sys

# build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('file_name', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of line to read' )
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0' )

args = parser.parse_args()

try:
    f = open(args.file_name)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
# parse the arguments
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])
