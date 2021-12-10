# author: Tamas Demian
# date: 2021-12-08

from scrambled import *
import logging		# https://docs.python.org/3.4/library/logging.html
import argparse		# https://docs.python.org/3/library/argparse.html
import pathlib

def main():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawTextHelpFormatter,
		description='Count scrambled occurrences of dictionary items for each input line.', 
		epilog='''EXAMPLE (before build): 
  python scrambled-strings.py --dictionary ../data/dict.txt --input ../data/input.txt --loglevel DEBUG
EXAMPLE (after build):
         scrambled-strings    --dictionary ../data/dict.txt --input ../data/input.txt --loglevel DEBUG''')
	parser.add_argument('--dictionary', type=pathlib.Path, nargs=1, help='path of dictionary file', metavar=('DICT'), required=True)
	parser.add_argument('--input', type=pathlib.Path, nargs=1, help='path of input file', required=True)
	parser.add_argument('--loglevel', nargs='?', help='log level. DEBUG displays dictionary and matches', choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], required=False)
	args = parser.parse_args()
	# TODO print_help instead of print_usage in case of arg constraint violation

	if args.loglevel is None:
		logging.basicConfig(level="INFO")
	else:
		logging.basicConfig(level=args.loglevel)

	try:
		d=processDictionary(str(args.dictionary[0]))
		processInput(str(args.input[0]),d)
	except Exception as ex:
		logging.error(ex)
		parser.print_help(file=None)
		exit()

if __name__ == '__main__':
    main()


