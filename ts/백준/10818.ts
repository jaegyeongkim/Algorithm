// LINK: https://www.acmicpc.net/problem/10818

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5, 20, 10, 35, 30, 7];

const N = input[0];

let max = -Infinity;
let min = Infinity;

for (let i = 1; i < N + 1; i++) {
  max = Math.max(max, input[i]);
  min = Math.min(min, input[i]);
}

console.log(min, max);
