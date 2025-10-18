// LINK: https://www.acmicpc.net/problem/2839

import * as fs from "fs";

const total = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

const exceedCount = Math.ceil(total / 3) + 1;
let answer = -1;

for (let i = 0; i < exceedCount; i++) {
  if (answer !== -1) break;
  for (let j = 0; j < exceedCount; j++) {
    if (answer !== -1) break;

    const value = 3 * i + 5 * j;

    if (value > total) break;
    if (value === total) {
      answer = i + j;
    }
  }
}

console.log(answer);
