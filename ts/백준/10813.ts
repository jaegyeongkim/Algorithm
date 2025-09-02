// LINK: https://www.acmicpc.net/problem/10813

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5, 4, 1, 2, 3, 4, 1, 4, 2, 2];

const N = input[0];
const M = input[1];
const arr: number[] = [];

for (let i = 0; i < N; i++) {
  arr.push(i + 1);
}

for (let i = 0; i < M; i++) {
  const index1 = input[i * 2 + 2];
  const index2 = input[i * 2 + 3];

  const before = arr[index1 - 1];
  arr[index1 - 1] = arr[index2 - 1];
  arr[index2 - 1] = before;
}

console.log(arr.join(" "));
