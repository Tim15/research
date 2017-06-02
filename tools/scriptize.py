#!/usr/bin/env python3
def shebang(path, s):
    with open(path, "r+") as file:
        if s not in file.readline():
            file.seek(0, 0)
            content = file.read()
            file.seek(0, 0)
            file.write(s.rstrip('\r\n') + '\n' + content)
def copyright(path):
    with open(path, "r+") as f:
        content = f.readlines()
        copyright = """Licensed to loqu, inc. (Loqu) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Loqu licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
        """
# Copyright (c) 2017 loqu, inc. All Rights Reserved.
# This work is licensed to loqu, inc. (Loqu) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Loqu licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
        i = 1 # start at second line, already includes shebang
        for line in copyright.split("\n"):
            content.insert(i, line)
            i += 1
        w = "\n".join(content)
        print(w)
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
                copyright(l)
                make_executable(l)
