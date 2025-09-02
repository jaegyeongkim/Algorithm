// LINK: https://www.acmicpc.net/problem/25304

import * as fs from "fs";

// const input = [260000, 4, 20000, 5, 30000, 2, 10000, 6, 5000, 8];
// const input = [250000, 4, 20000, 5, 30000, 2, 10000, 6, 5000, 8];

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const X = input[0];
const N = input[1];
const arr = input.splice(2);

let sum = 0;

for (let i = 0; i < N; i++) {
  sum += arr[i * 2] * arr[i * 2 + 1];
}

console.log(X === sum ? "Yes" : "No");
