#!/usr/bin/env python3
#!/usr/bin/env python
if __name__ == "__main__":
    import anyfile
    with anyfile.AnyFile("./tests.py") as a:
        with open("./tests.py") as b:
            assert a == b
    with anyfile.AnyFile("http://google.com") as c:
        r = requests.get("http://google.com")
        assert r == '\n'.join(c.readlines())
