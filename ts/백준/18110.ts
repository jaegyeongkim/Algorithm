// LINK: https://www.acmicpc.net/problem/18110

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const N = input[0];

if (N === 0) {
  console.log(0);
} else {
  const arr = input.splice(1).sort((a, b) => a - b);
  const round = Math.round(N * 0.15);

  let total = 0;

  arr.splice(round, N - round * 2).forEach((num) => {
    total += num;
  });

  console.log(Math.round(total / (N - round * 2)));
}
