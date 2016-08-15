import os
import sys

path = os.path.dirname(os.path.realpath(__file__))
print("test file path is " + path)
path = path[:path.rfind("/")]
path = path[:path.rfind("/")]
print("adding module path: " + path);
sys.path.append(path)


import program as p

if (p.add(99, 1) != 100):
    sys.exit(1)

if (p.sub(99, 50) != 49):
    sys.exit(2)

if (p.mult(12, 10) != 120):
    sys.exit(3)

if (p.div(12, 4) != 3):
    sys.exit(4)

print("program_spec tests passed");
sys.exit(0)
