// LINK: https://www.acmicpc.net/problem/11021

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5, 1, 1, 2, 3, 3, 4, 9, 8, 5, 2];

const T = input[0];
const arr = input.splice(1);

for (let i = 0; i < T; i++) {
  console.log(`Case #${i + 1}:`, arr[i * 2] + arr[i * 2 + 1]);
}
