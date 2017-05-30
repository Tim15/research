#!/usr/bin/env python3
#!/usr/bin/env python
import requests

class AnyFile():
    def __init__(self, location):
        self.loc = location
    def __enter__(self):
        try:
            return __r__(self.loc)
        except:
            loc = "./tmp/" + os.path.basename(os.path.normpath(self.loc))
            r = requests.get(self.loc)
            with open(loc, "w") as write_file:
                write_file.write(r)
            return __r__(loc)
    def __r__(self, loc):
        with open(loc, "r") as file:
            return file
    def __exit__(self, type, value, traceback):
        self.cr.restore()
