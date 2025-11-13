// LINK: https://www.acmicpc.net/problem/1920

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const A = input.slice(1, N + 1);
const M = input[N + 1];
const arr = input.slice(N + 2, N + M + 2);

const obj = new Set(A);

for (let i = 0; i < M; i++) {
  console.log(obj.has(arr[i]) ? 1 : 0);
}
