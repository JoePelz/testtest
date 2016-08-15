describe("Basic Arithmetic", function() {

  it("has a sum function", function() {
    expect(sum(1, 1, 1)).toBe(3);
    expect(sum(1, 1, 2)).toBe(4);
    expect(sum(1, 7, 2)).toBe(10);
    expect(sum(-3, -5, 8)).toBe(0);
  });

  it("has a average function", function() {
    expect(avg(1, 1, 1)).toBeCloseTo(1, 3);
    expect(avg(100, 0, -100)).toBeCloseTo(0, 3);
    expect(avg(30, 50, 70)).toBeCloseTo(50, 3);
    expect(avg(40, 50, 70)).toBeCloseTo(53.333, 2);
  });

  it("has a midpoint function", function() {
    expect(mid(2, 5, 8)).toBe(8);
    expect(mid(2, 8, 5)).toBe(8);
    expect(mid(5, 8, 2)).toBe(8);
    expect(mid(5, 2, 8)).toBe(8);
    expect(mid(8, 2, 5)).toBe(8);
    expect(mid(8, 5, 2)).toBe(8);
  });
});


