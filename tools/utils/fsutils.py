def rline(file, line):
    """Deletes line from file"""
    with open(file, "r") as input:
        with open(file, "wb") as output: 
            for l in input:
                if l != line + "\n":
                    output.write(l)
