// LINK: https://www.acmicpc.net/problem/10951

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [1, 1, 2, 3, 3, 4, 9, 8, 5, 2];

const N = input.length;

for (let i = 0; i < N / 2; i++) {
  console.log(input[i * 2] + input[i * 2 + 1]);
}
