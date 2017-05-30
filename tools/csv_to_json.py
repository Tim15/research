#!/usr/bin/env python3
#!/usr/bin/python
import argparse

"""
Simple tool to parse csv files (optionally with provided headers) into JSON
"""

p = argparse.ArgumentParser(description="Simple tool to parse csv files (optionally with provided headers) into JSON")
p.add_argument("location", help="location of csv file")
p.add_argument("--csv_headers", action="store_true", help="boolean - represents whether the csv contains a header row. If not, headers must be provided with --headers")
p.add_argument("--headers", help="list of comma-seperated headers. will override the headers provided in the csv file. make sure they line up with the csv file")
args = p.parse_args()

headers = []
values = []
out = ""

if(args.location):
    with open(args.location) as f:
        for idx, l in enumerate(f.readlines()):
            for token in l.split(","):
                if idx == 0:
                    if args.csv_headers == True:
                        headers.append(token)
                else:
                    values.append(token)
        headers = args.headers.split(",")
        out += "[{"
        for idx, val in enumerate(values):
            r = idx%len(headers)
            if r==0 and idx > 0:
                out += "\b},{"
            out += '"%s":"%s",'%(headers[r].strip(),val.strip())
        out += "\b}]"

    print(out)
