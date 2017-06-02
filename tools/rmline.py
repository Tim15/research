#!/usr/bin/env python3
print("hello");
import os
print(os.getcwd())
for root, dirs, filenames in os.walk(os.getcwd()):
	for f in filenames:
	    if ".py" in f and ".pyc" not in f and "__init__.py" not in f and "fsutils" not in f:
		l = os.path.join(root, f)
		print(l)
		with open(l, 'r') as fin:
		    data = fin.read().splitlines(True)
		with open(l, 'w') as fout:
		    fout.writelines(data[1:])
