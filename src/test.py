# author: Tamas Demian
# date: 2021-12-08

import subprocess
import unittest
import sys
from scrambled import *

class TestScrumbledStrings(unittest.TestCase):

	def test_normalize(self):
		self.assertEqual(normalize("aihgfedcba"), normalize("ghiadefabc"))

	def test_processingDictionary(self):
		d=processDictionary("../data/dict.txt")
		self.assertEqual(d,
			{'a': [{'middle': 'apx', 'lastChar': 'j', 'original': 'axpaj', 'len': 5, 'used': False}, 
				{'middle': 'apx', 'lastChar': 'j', 'original': 'apxaj', 'len': 5, 'used': False}, 
				{'middle': 'b', 'lastChar': 'd', 'original': 'abd', 'len': 3, 'used': False}], 
			'd': [{'middle': 'bnr', 'lastChar': 't', 'original': 'dnrbt', 'len': 5, 'used': False}], 
			'p': [{'middle': 'djx', 'lastChar': 'n', 'original': 'pjxdn', 'len': 5, 'used': False}], 
			'b': [], 'c': [],
			'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 
			'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
		)

	def test_processingInput(self):
		if not hasattr(sys.stdout, "getvalue"):
			self.fail("need to run in buffered mode")
		d=processDictionary("../data/dict.txt")
		result=processInput("../data/input.txt",d)
		output = sys.stdout.getvalue()
		self.assertEqual(output, "Case #1: 4\nCase #2: 4\n")

	@unittest.skip("subprocess installation problem")
	def test_CLI(self):
		pytonCommand=subprocess.run("which python", capture_output=True).stdout # where command in Windows
		response=subprocess.run(pythonCommand + " scrambled-strings.py --dictionary ../data/dict.txt --input ../data/input.txt", capture_output=True)
		self.assertEqual(response.stdout, "Case #1: 4\n")

if __name__ == '__main__':
    unittest.main(buffer=True)
