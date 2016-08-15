function sum(a, b, c) {
  return a + b + c;
}

function avg(a, b, c) {
  return sum(a, b, c) / 3;
}

function mid(a, b, c) {
  if (a < b) {
    if (b < c) {
        return (c + a) / 2;
    } else if (a < c) {
        return (b + a) / 2;
    } else {
        return (c + b) / 2;
    }
  } else {
    if (c < b) {
        return (a + c) / 2;
    } else if (c < a) {
        return (a + b) / 2;
    } else {
        return (c + b) / 2;
    }
  }
  return b;
}
