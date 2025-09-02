// LINK: https://www.acmicpc.net/problem/8393

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const n = input[0];

let sum = 0;
for (let i = 1; i <= n; i++) {
  sum += i;
}

console.log(sum);
