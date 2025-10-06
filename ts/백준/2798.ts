// https://www.acmicpc.net/problem/2798

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const M = input[1];
const arr = input.splice(2);

let minChar = Infinity;

for (let i = 0; i < N - 2; i++) {
  if (minChar === 0) break;
  for (let j = i + 1; j < N - 1; j++) {
    if (minChar === 0) break;
    for (let k = j + 1; k < N; k++) {
      if (minChar === 0) break;
      const sum = arr[i] + arr[j] + arr[k];

      if (M >= sum && M - sum < minChar) {
        minChar = M - sum;
      }
    }
  }
}

console.log(M - minChar);
