// LINK: https://www.acmicpc.net/problem/10807

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [11, 1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4, 2];

// const input = [11, 1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4, 5];

const N = input[0];
const arr = input.slice(1, N + 1);
const number = input[input.length - 1];
let count = 0;

for (let i = 0; i < N; i++) {
  if (arr[i] === number) {
    count += 1;
  }
}

console.log(count);
