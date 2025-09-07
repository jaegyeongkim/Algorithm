// LINK: https://www.acmicpc.net/problem/2563

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = Array.from({ length: 100 }, () =>
  Array.from({ length: 100 }, () => 0)
);

for (let n = 1; n < N + 1; n++) {
  const w = input[n * 2 - 1] - 1;
  const h = input[n * 2] - 1;

  for (let i = h; i < h + 10; i++) {
    for (let j = w; j < w + 10; j++) {
      arr[i][j] = 1;
    }
  }
}

let sum = 0;

for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 100; j++) {
    if (arr[i][j] === 1) {
      sum += 1;
    }
  }
}

console.log(sum);
