// LINK: https://www.acmicpc.net/problem/2738

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
// const input = [3, 3, 1, 1, 1, 2, 2, 2, 0, 1, 0, 3, 3, 3, 4, 4, 4, 5, 5, 100];
// const input = [1, 1, 1, 1];
// const input = [1, 2, 1, 1, 1, 1];
// const input = [2, 2, 1, 1, 1, 1, 2, 2, 2, 3];

const N = input[0];
const M = input[1];
const arr = input.splice(2);

const length = N * M;

for (let i = 0; i < N; i++) {
  const newArr: number[] = [];

  for (let j = 0; j < M; j++) {
    newArr.push(arr[i * M + j] + arr[i * M + j + length]);
  }

  console.log(newArr.join(" "));
}
