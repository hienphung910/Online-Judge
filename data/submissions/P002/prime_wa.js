// Thuat toan dung nhung in chu thuong -> comparator "exact" cho WA.
// Minh hoa: cung mot loi logic trinh bay bi bat o moi ngon ngu.
const data = require("fs").readFileSync(0, "utf8").trim().split(/\s+/);
const t = Number(data[0]);

function isPrime(n) {
  if (n < 2n) return false;
  if (n % 2n === 0n) return n === 2n;
  for (let i = 3n; i * i <= n; i += 2n) {
    if (n % i === 0n) return false;
  }
  return true;
}

const out = [];
for (let i = 1; i <= t; i++) {
  out.push(isPrime(BigInt(data[i])) ? "yes" : "no");
}
console.log(out.join("\n"));
