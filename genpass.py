"""
Generate a cryptographically secure password.
"""

import sys
import random
import string
import argparse

def genpass(length):

     characters = string.letters + string.digits + string.punctuation

     return ''.join(random.SystemRandom().choice(characters) for _ in range(length))

if __name__ == "__main__":

     parser = argparse.ArgumentParser()
     parser.add_argument('-l', '--length', help='Password length desired.'
                         , default=32, type=int)
     args = parser.parse_args()

     print(genpass(args.length))
