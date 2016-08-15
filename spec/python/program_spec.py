import program as p
import sys

if (p.add(99, 1) != 100):
  sys.exit(1)

if (p.sub(99, 50) != 49):
  sys.exit(2)

if (p.mult(12, 10) != 120):
  sys.exit(3)

if (p.div(12, 4) != 3):
  sys.exit(4)

sys.exit(0)
