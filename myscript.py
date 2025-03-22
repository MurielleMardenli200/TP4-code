import os
import sys

os.system("git bisect start $badhash $goodhash")
exit_code = os.system("git bisect run")

os.system("git bisect reset")
sys.exit(exit_code)