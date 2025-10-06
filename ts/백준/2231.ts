// https://www.acmicpc.net/problem/2231

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

let answer = 0;

for (let i = 0; i < N; i++) {
  if (answer) break;

  let sum = i;

  String(i)
    .split("")
    .forEach((n) => {
      sum += Number(n);
    });
  if (sum === N) {
    answer = i;
  }
}

console.log(answer);
