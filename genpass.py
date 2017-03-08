"""
Generate a cryptographically secure password
"""

import sys
import string
import random

def genpass(length=32):

     return ''.join(random.SystemRandom().choice(string.letters + string.digits) for _ in range(length))


if __name__=="__main__":

     length = 32

     if len(sys.argv) > 1:
          length = int(sys.argv[1])

     print(genpass(length))
