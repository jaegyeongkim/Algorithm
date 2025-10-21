// LINK: https://www.acmicpc.net/problem/30802

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\n+/);

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const [T, P] = input[2].split(" ").map(Number);

let cnt = 0;
arr.forEach((num) => {
  cnt += Math.ceil(num / T);
});

const q = Math.floor(N / P);
console.log(cnt);
console.log(q, N % P);
