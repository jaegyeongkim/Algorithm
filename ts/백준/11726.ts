// LINK: https://www.acmicpc.net/problem/11726

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));

const combination = (n: number, r: number): number => {
  if (r === 0) return 1;
  if (r === 1) return n;
  if (n === r) return 1;

  let result = 1;

  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  for (let i = 1; i <= r; i++) {
    result /= i;
  }
  for (let i = 1; i <= n - r; i++) {
    result /= i;
  }

  return result;
};

let sum = 0;
let oddCount = N % 2 === 0 ? 0 : 1;

while (1) {
  const n = oddCount + (N - oddCount) / 2;
  const r = oddCount;

  sum += combination(n, r);

  oddCount += 2;
  if (oddCount > N) break;
}

console.log(sum % 10007);
