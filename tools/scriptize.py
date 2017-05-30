#!/usr/bin/env python3
#!/usr/bin/env python
def shebang(path, s):
    with open(path, "r+") as file:
        if s not in file.readline():
            file.seek(0, 0)
            content = file.read()
            file.seek(0, 0)
            file.write(s.rstrip('\r\n') + '\n' + content)

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

if __name__ == "__main__":
    import os
    for root, dirs, filenames in os.walk(os.getcwd()):
        for f in filenames:
            if ".py" in f and ".pyc" not in f:
                l = os.path.join(root, f)
                shebang(l, "#!/usr/bin/env python3")
                make_executable(l)
