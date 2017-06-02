#!/usr/bin/env python3
import argparse

"""
Simple tool to parse whitespace data files into CSV files
"""

p = argparse.ArgumentParser(description="Simple tool to parse csv files (optionally with provided headers) into JSON")
p.add_argument("input", help="location of whitespace data file")
p.add_argument("out", help="location of csv file to write to disk")
args = p.parse_args()

out = "";
with open(args.input, "r") as f:
    for l in f.readlines():
        out += l.replace(" ", ",", 1).strip()
with open(args.out, "w") as f:
    f.write(out)
