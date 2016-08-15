def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def div(a, b):
  return a / float(b)

if __name__ == "__main__":
  a = 13
  b = 7
  
  print("a is " + str(a))
  print("b is " + str(b))
  print("a + b is " + str(add(a, b)))
  print("a - b is " + str(sub(a, b)))
  print("a * b is " + str(mult(a, b)))
  print("a / b is " + str(div(a, b)))
