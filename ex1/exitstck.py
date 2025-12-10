from contextlib import ExitStack

paths = ["a.txt", "b.txt", "c.txt"]
with ExitStack() as stack:
    files = [stack.enter_context(open(p, "w")) for p in paths]
    for f in files:
        f.write("test\n")