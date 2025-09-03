// LINK: https://www.acmicpc.net/problem/3052

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// const input = [42, 84, 252, 420, 840, 126, 42, 84, 420, 126];

const N = input.length;
const arr = new Map();

for (let i = 0; i < N; i++) {
  arr.set(input[i] % 42, input[i] % 42);
}

console.log(arr.size);
