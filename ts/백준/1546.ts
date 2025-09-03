// LINK: https://www.acmicpc.net/problem/1546

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [4, 10, 20, 0, 100];

const N = input[0];
const max = Math.max(...input.slice(1));
let sum = 0;

for (let i = 1; i < N + 1; i++) {
  sum += (input[i] / max) * 100;
}
console.log(sum / N);
