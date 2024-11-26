import os
import sys

lab6_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab6_root)

from interface import main

if __name__ == "__main__":
    main()
