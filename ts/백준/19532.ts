// https://www.acmicpc.net/problem/19532

import * as fs from "fs";

const [a, b, c, d, e, f] = fs
  .readFileSync(0, "utf8")
  .trim()
  .split(/\s+/)
  .map(Number);

const answer = [];

for (let x = -999; x <= 999; x++) {
  if (answer.length) break;
  for (let y = -999; y <= 999; y++) {
    if (answer.length) break;
    if (a * x + b * y === c && d * x + e * y === f) {
      answer.push(x);
      answer.push(y);
    }
  }
}

console.log(answer.join(" "));
