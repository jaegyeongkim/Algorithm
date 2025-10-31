// LINK: https://www.acmicpc.net/problem/7568

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = Array(N).fill(1);

for (let i = 0; i < N - 1; i++) {
  const x = input[i * 2 + 1];
  const y = input[i * 2 + 2];

  for (let j = i + 1; j < N; j++) {
    const x2 = input[j * 2 + 1];
    const y2 = input[j * 2 + 2];
    if (x < x2 && y < y2) {
      arr[i]++;
    } else if (x > x2 && y > y2) {
      arr[j]++;
    }
  }
}

console.log(arr.join(" "));
