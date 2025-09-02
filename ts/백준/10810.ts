// LINK: https://www.acmicpc.net/problem/10810

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5, 4, 1, 2, 3, 3, 4, 4, 1, 4, 1, 2, 2, 2];

const N = input[0];
const M = input[1];
const basket = new Array(N).fill(0);

for (let a = 0; a < M; a++) {
  const i = input[a * 3 + 2];
  const j = input[a * 3 + 3];
  const k = input[a * 3 + 4];
  for (let b = i; b < j + 1; b++) {
    basket[b - 1] = k;
  }
}

console.log(basket.join(" "));
