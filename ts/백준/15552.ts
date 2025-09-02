// LINK: https://www.acmicpc.net/problem/15552

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
// const input = [5, 1, 1, 12, 34, 5, 500, 40, 60, 1000, 1000];

const T = input[0];
const arr = input.splice(1);
let sum = "";

for (let i = 0; i < T; i++) {
  sum += `${arr[i * 2] + arr[i * 2 + 1]}`;
  if (i !== T - 1) {
    sum += "\n";
  }
}

console.log(sum);
